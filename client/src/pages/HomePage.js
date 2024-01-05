import React from "react";
import StarryBackground from "../components/StarryBackground";
import Navbar from "../components/Navbar";
import LoginCard from "./LoginPage";
import Register from "./Register";
import Description from "../components/Description";

export default function HomePage() {
  return (
    <div>
      <StarryBackground />
      <Navbar />
      <Description />

    </div>
  );
}
