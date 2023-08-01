import React from 'react';
import { Canvas } from 'react-three-fiber';

const Graph = ({ dataX, dataY }) => {
  return (
    <Canvas>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      <axesHelper args={[5]} />
      {dataX.map((x, index) => (
        <mesh key={index} position={[x * 0.1, dataY[index] * 0.1, 0]}>
          <sphereGeometry args={[0.1, 16, 16]} />
          <meshStandardMaterial color="red" />
        </mesh>
      ))}
    </Canvas>
  );
};

export default Graph;