import React from "react";
import "./navbar.css"

export default function Navbar() {
    return (
        <>
            <nav className="navbar">
                <div className="mx-auto px-2">
                    <div className="flex items-center justify-between h-16 bg-opacity-0">
                        <span className="text-2xl text-white font-semibold px-3"><a href="/">Logo</a></span>
                        <div className="flex space-x-4 text-white">
                            <a href="/" className="px-3">Attendance</a>
                            <a href="/" className="px-3">About</a>
                            <a href="/" className="px-3">Register</a>
                            <a href="/pages/Login" className="px-3">LogIn</a>
                        </div>
                    </div>
                </div>
            </nav>
        </>
    );
}