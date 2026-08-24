import {Config} from '@remotion/cli/config';

Config.setEntryPoint('./src/index.ts');
Config.setChromiumOpenGlRenderer('angle');
Config.setBrowserExecutable('/usr/bin/google-chrome-stable');
Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
