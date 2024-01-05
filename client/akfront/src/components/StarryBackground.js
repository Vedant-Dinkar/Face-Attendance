import React, { useRef, useEffect } from 'react';
import * as THREE from 'three';

const StarryBackground = () => {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer();
  const warpRef = useRef();

  useEffect(() => {
    // Set up renderer
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Create warp speed effect using streaks
    const warpMaterial = new THREE.LineBasicMaterial({ color: 0xFFFFFF, linewidth: 0.1 });
    const warpGeometry = new THREE.BufferGeometry();

    const warpVertices = [];
    for (let i = 0; i < 50; i++) {
      const x = (Math.random() - 0.5) * 100;
      const y = (Math.random() - 0.5) * 100;
      const z = (Math.random() - 0.5) * 100;
      warpVertices.push(x, y, z);
    }

    warpGeometry.setAttribute('position', new THREE.Float32BufferAttribute(warpVertices, 3));

    const warp = new THREE.Line(warpGeometry, warpMaterial);
    scene.add(warp);

    // Set up camera position
    camera.position.z = 5;

    // Animation loop
    const animate = function () {
      requestAnimationFrame(animate);

      // Move the warp effect
      warp.rotation.x += 0.0005;
      warp.rotation.y += 0.0005;

      renderer.render(scene, camera);
    };

    // Handle window resize
    const handleResize = () => {
      const newWidth = window.innerWidth;
      const newHeight = window.innerHeight;

      camera.aspect = newWidth / newHeight;
      camera.updateProjectionMatrix();

      renderer.setSize(newWidth, newHeight);
    };

    window.addEventListener('resize', handleResize);

    // Set warpRef current to the warp object for external manipulation
    warpRef.current = warp;

    // Start animation
    animate();

    // Clean up event listener on component unmount
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return null; // This component doesn't render anything directly, it's handled by Three.js
};

export default StarryBackground;
