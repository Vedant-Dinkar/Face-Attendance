import React from "react";
import StarryBackground from "../components/StarryBackground";
import Navbar from "../components/Navbar";
import LoginCard from "./Login";
import Register from "./Register";
import Description from "../components/Description";

export default function HomePage() {
  return (
    <div>
      <StarryBackground />
      <Navbar />
      <div className="absolute top-0 left-0 w-full h-full flex flex-col items-center justify-center">
        <Description />
      </div>
    </div>
  );
}
