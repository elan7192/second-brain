import React from 'react';
import {Composition} from 'remotion';
import {GraphDemo} from './GraphDemo';
import graph from './graph.json';

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="GraphDemo"
      component={GraphDemo}
      durationInFrames={300}
      fps={30}
      width={1280}
      height={720}
      defaultProps={{graph}}
    />
  );
};
