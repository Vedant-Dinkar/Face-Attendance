import React, { useEffect } from 'react';
import particlesJS from 'particles.js';

const Particles = () => {
  useEffect(() => {
    particlesJS('particles-js', {

    });
  }, []);

  return <div id="particles-js"></div>;
};

export default Particles;

