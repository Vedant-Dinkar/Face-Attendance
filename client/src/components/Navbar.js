import React from "react";
import { Button } from "@nextui-org/react";
import { Link } from "react-router-dom";
import logo from '../logo192.png';
import "./navbar.css";

export default function Navbar() {
    return (
        <nav className="navbar">
            <div className="mx-auto px-2">
                <div className="flex items-center justify-between h-16 bg-opacity-0 bg-gradient-to-r from-danger to-danger">
                    <span className="text-2xl text-white font-semibold px-3">
                        <Link to="/">
                            <img src={logo} alt="Logo" className="h-10" />
                        </Link>
                    </span>
                    <div className="flex space-x-4 text-white">
                        <Link to="/upload" className="text-white">
                            <Button className="w-24 bg-gradient-to-r from-danger to-danger font-bold my-4" radius="sm">Upload</Button>
                        </Link>
                        <Link to="/" className="text-white">
                            <Button className="w-24 bg-gradient-to-r from-danger to-danger font-bold my-4" radius="sm">About</Button>
                        </Link>
                        <Link to="/login" className="text-white">
                            <Button className="w-24 bg-gradient-to-r from-danger to-danger font-bold my-4" radius="sm">Login</Button>
                        </Link>
                        <Link to="/register" className="text-white">
                            <Button className="w-24 bg-gradient-to-r from-danger to-danger font-bold my-4" radius="sm">Register</Button>
                        </Link>
                    </div>
                </div>
            </div>
        </nav>
    );
}
