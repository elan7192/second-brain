import React, {useMemo} from 'react';
import {AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {ThreeCanvas} from '@remotion/three';
import {useThree} from '@react-three/fiber';
import * as THREE from 'three';

type GraphNode = {
  id: string;
  title: string;
  type: string;
  cluster: string;
  path: string;
  x: number;
  y: number;
  z?: number;
};

type GraphEdge = {
  source: string;
  target: string;
  cx: number;
  cy: number;
  intra: boolean;
};

export type GraphData = {
  nodes: GraphNode[];
  edges: GraphEdge[];
  colors: Record<string, string>;
  labels: Record<string, string>;
  types: Record<string, string>;
  legend: {key: string; label: string; color: string}[];
  centers: Record<string, [number, number, number]>;
  headers: Record<string, [number, number]>;
  heights: Record<string, number>;
};

type CameraShot = {
  position: THREE.Vector3;
  target: THREE.Vector3;
  dist: number;
};

const FOV = 46;
const CLUSTER_DELAY: Record<string, number> = {
  bridge: 0,
  compile: 4,
  memory: 7,
  verification: 10,
  harness: 13,
  'hunt-ship': 16,
  nav: 19,
};

function worldOf(n: GraphNode): THREE.Vector3 {
  return new THREE.Vector3(n.x, n.z || 0, n.y);
}

function nodeRadius(n: GraphNode): number {
  if (n.id === 'agent-operating-system') return 7.2;
  if (n.id === 'Home') return 5.8;
  if (n.type === 'concept' || n.type === 'meta') return 4.6;
  return 3.8;
}

function shotAt(frame: number): CameraShot {
  const target = new THREE.Vector3(0, 8, 10);
  const orbit = interpolate(frame, [0, 300], [0.18, 1.28], {
    easing: Easing.inOut(Easing.cubic),
  });
  const dist = interpolate(frame, [0, 80, 160, 230, 300], [540, 440, 285, 188, 172], {
    easing: Easing.inOut(Easing.cubic),
  });
  const position = new THREE.Vector3(
    target.x + Math.sin(orbit) * dist * 0.48,
    target.y + dist * 0.52,
    target.z + Math.cos(orbit) * dist * 0.78,
  );
  return {position, target, dist};
}

function project(
  vec: THREE.Vector3,
  shot: CameraShot,
  width: number,
  height: number,
): {x: number; y: number; behind: boolean} {
  const camera = new THREE.PerspectiveCamera(FOV, width / height, 1, 2000);
  camera.position.copy(shot.position);
  camera.lookAt(shot.target);
  camera.updateMatrixWorld();
  const v = vec.clone().project(camera);
  return {
    x: (v.x * 0.5 + 0.5) * width,
    y: (-v.y * 0.5 + 0.5) * height,
    behind: v.z > 1,
  };
}

function overlap(
  a: {x: number; y: number; w: number; h: number},
  b: {x: number; y: number; w: number; h: number},
): boolean {
  const p = 6;
  return !(a.x + a.w + p < b.x || b.x + b.w + p < a.x || a.y + a.h + p < b.y || b.y + b.h + p < a.y);
}

function measure(text: string, weight: string): number {
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  if (!ctx) return text.length * 7.2;
  ctx.font = `${weight} 12px "Segoe UI Variable", "SF Pro Text", "Helvetica Neue", sans-serif`;
  return ctx.measureText(text).width;
}

const CameraRig: React.FC<{shot: CameraShot}> = ({shot}) => {
  const {camera} = useThree();
  camera.position.copy(shot.position);
  camera.lookAt(shot.target);
  camera.updateProjectionMatrix();
  return null;
};

const SceneFog: React.FC = () => {
  const {scene} = useThree();
  scene.background = new THREE.Color(0x090b10);
  scene.fog = new THREE.Fog(0x090b10, 220, 760);
  return null;
};

const NodeMesh: React.FC<{
  node: GraphNode;
  color: string;
  scale: number;
  opacity: number;
  hot: boolean;
}> = ({node, color, scale, opacity, hot}) => {
  const pos = worldOf(node);
  return (
    <mesh position={[pos.x, pos.y, pos.z]} scale={scale}>
      <sphereGeometry args={[1, 24, 18]} />
      <meshStandardMaterial
        color={color}
        roughness={0.38}
        metalness={0.22}
        emissive={color}
        emissiveIntensity={hot ? 0.78 : 0.16}
        transparent={opacity < 1}
        opacity={opacity}
      />
    </mesh>
  );
};

const EdgeTube: React.FC<{
  a: GraphNode;
  b: GraphNode;
  rec: GraphEdge;
  opacity: number;
  hot: boolean;
}> = ({a, b, rec, opacity, hot}) => {
  const geom = useMemo(() => {
    const p0 = worldOf(a);
    const p2 = worldOf(b);
    const p1 = new THREE.Vector3(
      rec.cx,
      ((a.z || 0) + (b.z || 0)) / 2 + (rec.intra ? 10 : 16),
      rec.cy,
    );
    const curve = new THREE.QuadraticBezierCurve3(p0, p1, p2);
    return new THREE.TubeGeometry(curve, 14, rec.intra ? 0.72 : 0.48, 6, false);
  }, [a, b, rec]);
  return (
    <mesh geometry={geom}>
      <meshStandardMaterial
        color={rec.intra ? '#ddd4bf' : '#b4aa97'}
        roughness={0.5}
        metalness={0.12}
        emissive={'#3a342c'}
        emissiveIntensity={hot ? 0.55 : rec.intra ? 0.22 : 0.12}
        transparent
        opacity={opacity}
      />
    </mesh>
  );
};

const Labels: React.FC<{
  graph: GraphData;
  shot: CameraShot;
  headerAlpha: number;
  labelAlpha: number;
  focus: GraphNode | null;
  width: number;
  height: number;
}> = ({graph, shot, headerAlpha, labelAlpha, focus, width, height}) => {
  const adj = useMemo(() => {
    const map = new Map<string, string[]>();
    for (const e of graph.edges) {
      if (!map.has(e.source)) map.set(e.source, []);
      if (!map.has(e.target)) map.set(e.target, []);
      map.get(e.source)!.push(e.target);
      map.get(e.target)!.push(e.source);
    }
    return map;
  }, [graph.edges]);

  const items: React.ReactNode[] = [];
  const placed: {x: number; y: number; w: number; h: number}[] = [];

  if (headerAlpha > 0.02) {
    for (const [cluster, pos] of Object.entries(graph.headers)) {
      const center = graph.centers[cluster];
      let p = project(
        new THREE.Vector3(pos[0], (graph.heights[cluster] || 0) + 18, pos[1]),
        shot,
        width,
        height,
      );
      if (
        p.behind ||
        p.x < 90 ||
        p.x > width - 90 ||
        p.y < 100 ||
        p.y > height - 70
      ) {
        p = project(
          new THREE.Vector3(center[0], (graph.heights[cluster] || 0) + 18, center[1]),
          shot,
          width,
          height,
        );
      }
      if (p.behind) continue;
      const title = (graph.labels[cluster] || cluster).toUpperCase();
      const tw = measure(title, '600');
      placed.push({x: p.x - tw / 2 - 6, y: p.y - 9, w: tw + 12, h: 18});
      items.push(
        <div
          key={'h-' + cluster}
          style={{
            position: 'absolute',
            left: p.x,
            top: p.y,
            transform: 'translate(-50%, -50%)',
            color: '#d2c9b4',
            fontSize: 12,
            fontWeight: 600,
            letterSpacing: '0.08em',
            opacity: headerAlpha,
            whiteSpace: 'nowrap',
          }}
        >
          {title}
        </div>,
      );
    }
  }

  const candidates = graph.nodes
    .map((n) => ({
      n,
      must: focus?.id === n.id,
      deg: (adj.get(n.id) || []).length,
    }))
    .filter((item) => item.must || labelAlpha > 0.08)
    .sort((a, b) => Number(b.must) - Number(a.must) || b.deg - a.deg);

  let shown = 0;
  const labeled: GraphNode[] = [];
  for (const item of candidates) {
    const n = item.n;
    if (!item.must && shown >= 12) continue;
    if (!item.must && labeled.some((pt) => Math.hypot(pt.x - n.x, pt.y - n.y) < 70)) continue;
    const p = project(worldOf(n), shot, width, height);
    if (p.behind) continue;
    const label = n.title;
    const tw = measure(label, item.must ? '600' : '400');
    const r = 10;
    const slots: [number, number][] = [
      [p.x + r + 8, p.y],
      [p.x - tw - r - 8, p.y],
      [p.x - tw / 2, p.y - r - 16],
      [p.x - tw / 2, p.y + r + 16],
      [p.x + r + 8, p.y - 18],
      [p.x + r + 8, p.y + 18],
    ];
    let box: {x: number; y: number; w: number; h: number; lx: number; ly: number} | null = null;
    for (const [lx, ly] of slots) {
      const rect = {x: lx - 5, y: ly - 9, w: tw + 10, h: 18, lx, ly};
      if (!placed.some((prev) => overlap(prev, rect))) {
        box = rect;
        break;
      }
    }
    if (!box) continue;
    placed.push(box);
    labeled.push(n);
    shown += 1;
    items.push(
      <div
        key={'n-' + n.id}
        style={{
          position: 'absolute',
          left: box.lx,
          top: box.ly,
          transform: 'translateY(-50%)',
          background: 'rgba(9,11,16,0.82)',
          color: item.must ? '#f8f4ea' : '#ddd6c8',
          fontSize: 12,
          fontWeight: item.must ? 600 : 400,
          padding: '2px 5px',
          borderRadius: 6,
          opacity: item.must ? 1 : labelAlpha,
          whiteSpace: 'nowrap',
          pointerEvents: 'none',
        }}
      >
        {label}
      </div>,
    );
  }

  return <>{items}</>;
};

export const GraphDemo: React.FC<{graph: GraphData}> = ({graph}) => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const shot = shotAt(frame);
  const headerAlpha = interpolate(shot.dist, [200, 250], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const labelAlpha = interpolate(shot.dist, [200, 250], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const zoomed = shot.dist < 250;
  const byId = Object.fromEntries(graph.nodes.map((n) => [n.id, n]));
  const focusId = interpolate(frame, [220, 236], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  }) > 0.5
    ? 'llm-wiki'
    : '';
  const focus = (focusId && byId[focusId]) || null;
  const keep = new Set<string>();
  if (focus) {
    keep.add(focus.id);
    for (const e of graph.edges) {
      if (e.source === focus.id) keep.add(e.target);
      if (e.target === focus.id) keep.add(e.source);
    }
  }

  return (
    <AbsoluteFill style={{background: '#090b10', fontFamily: 'Segoe UI Variable, SF Pro Text, Helvetica Neue, sans-serif'}}>
      <ThreeCanvas width={width} height={height} camera={{fov: FOV, near: 1, far: 2000, position: [70, 210, 360]}}>
        <CameraRig shot={shot} />
        <SceneFog />
        <ambientLight color={'#8a8478'} intensity={0.9} />
        <directionalLight color={'#f4efe4'} intensity={1.15} position={[90, 240, 130]} />
        <pointLight color={'#c6a35a'} intensity={0.4} distance={700} position={[-50, 90, 40]} />
        <directionalLight color={'#6f9e92'} intensity={0.28} position={[-120, 40, -80]} />
        {Object.entries(graph.centers).map(([cluster, spec]) => (
          <mesh
            key={'glow-' + cluster}
            position={[spec[0], graph.heights[cluster] || 0, spec[1]]}
            scale={[1, 0.42, 1]}
          >
            <sphereGeometry args={[spec[2] * 0.92, 24, 16]} />
            <meshBasicMaterial color={'#c6a35a'} transparent opacity={0.055} depthWrite={false} />
          </mesh>
        ))}
        {graph.edges.map((rec) => {
          const a = byId[rec.source];
          const b = byId[rec.target];
          if (!a || !b) return null;
          const bridge = rec.source === 'agent-operating-system' || rec.target === 'agent-operating-system';
          const related = !!(focus && keep.has(a.id) && keep.has(b.id));
          const show = zoomed || rec.intra || bridge || related;
          const dim = !!(focus && !related);
          const opacity = show ? (dim ? 0.12 : 0.92) : 0.04;
          return (
            <EdgeTube
              key={rec.source + '-' + rec.target}
              a={a}
              b={b}
              rec={rec}
              opacity={opacity}
              hot={related}
            />
          );
        })}
        {graph.nodes.map((n) => {
          const delay = CLUSTER_DELAY[n.cluster] || 0;
          const appear = interpolate(frame, [delay, delay + 16], [0.001, 1], {
            easing: Easing.out(Easing.cubic),
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          });
          const hot = focus?.id === n.id;
          const on = !focus || keep.has(n.id);
          const pulse = hot ? 1.18 : 1;
          return (
            <NodeMesh
              key={n.id}
              node={n}
              color={graph.colors[n.type] || '#8b8478'}
              scale={nodeRadius(n) * appear * pulse}
              opacity={on ? 1 : 0.22}
              hot={hot}
            />
          );
        })}
      </ThreeCanvas>
      <AbsoluteFill style={{pointerEvents: 'none'}}>
        <Labels
          graph={graph}
          shot={shot}
          headerAlpha={headerAlpha}
          labelAlpha={labelAlpha}
          focus={focus}
          width={width}
          height={height}
        />
      </AbsoluteFill>
      <div
        style={{
          position: 'absolute',
          top: 22,
          left: 22,
          right: 22,
          display: 'flex',
          alignItems: 'center',
          gap: 18,
          padding: '10px 14px',
          borderRadius: 16,
          background: 'rgba(14,16,22,0.78)',
          border: '1px solid rgba(255,255,255,0.08)',
        }}
      >
        <div>
          <div style={{color: '#c6a35a', fontSize: 10, fontWeight: 600, letterSpacing: '0.16em', textTransform: 'uppercase'}}>
            Compiled wiki
          </div>
          <div style={{color: '#f4efe4', fontSize: 18, fontWeight: 600}}>Second brain</div>
        </div>
        <div style={{display: 'flex', gap: 8, flexWrap: 'wrap'}}>
          {graph.legend.map((item) => (
            <span
              key={item.key}
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: 7,
                padding: '5px 10px',
                borderRadius: 999,
                border: '1px solid rgba(255,255,255,0.08)',
                color: '#9a9386',
                fontSize: 12,
              }}
            >
              <i style={{width: 8, height: 8, borderRadius: '50%', background: item.color, display: 'block'}} />
              {item.label}
            </span>
          ))}
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          top: 96,
          right: 22,
          width: 300,
          padding: 16,
          borderRadius: 16,
          background: 'rgba(14,16,22,0.78)',
          border: '1px solid rgba(255,255,255,0.08)',
          minHeight: 140,
        }}
      >
        <div style={{color: '#c6a35a', fontSize: 10, fontWeight: 600, letterSpacing: '0.16em', textTransform: 'uppercase'}}>
          {focus ? 'Selected page' : 'Page'}
        </div>
        <div style={{color: '#f4efe4', fontSize: 20, fontWeight: 600, letterSpacing: '-0.03em', margin: '6px 0'}}>
          {focus ? focus.title : 'Concept clusters'}
        </div>
        <div style={{color: '#c6a35a', fontFamily: 'ui-monospace, SF Mono, Menlo, monospace', fontSize: 11, wordBreak: 'break-all'}}>
          {focus ? focus.path : 'Island headers, then node labels'}
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          bottom: 18,
          left: '50%',
          transform: 'translateX(-50%)',
          padding: '8px 14px',
          borderRadius: 999,
          background: 'rgba(14,16,22,0.78)',
          border: '1px solid rgba(255,255,255,0.08)',
          color: '#9a9386',
          fontSize: 12,
          whiteSpace: 'nowrap',
        }}
      >
        Orbit · depth · LoD labels
      </div>
    </AbsoluteFill>
  );
};
