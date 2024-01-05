import React from 'react';

const Register = () => {
    return (
        <div className="flex items-center justify-center h-screen">
            <div className="bg-gray-800 bg-opacity-60 p-8 rounded shadow-md w-96 text-white transform hover:scale-110 transition-transform duration-500">
                <h2 className="text-3xl font-extrabold mb-4">Register</h2>
                <form>
                    <div className="mb-4">
                        <label htmlFor="username" className="block text-sm font-medium text-gray-300 mb-1">
                            Roll Number
                        </label>
                        <input
                            type="text"
                            id="username"
                            name="username"
                            className="mt-1 p-2 w-full bg-opacity-100 border rounded-md bg-gray-900 text-white focus:outline-none focus:ring focus:border-white transition-all duration-300"
                            placeholder="Enter roll number"
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="username" className="block text-sm font-medium text-gray-300 mb-1">
                            Name
                        </label>
                        <input
                            type="text"
                            id="username"
                            name="username"
                            className="mt-1 p-2 w-full bg-opacity-100 border rounded-md bg-gray-900 text-white focus:outline-none focus:ring focus:border-white transition-all duration-300"
                            placeholder="Enter the name"
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="password" className="block text-sm font-medium text-gray-300 mb-1">
                            Class
                        </label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            className="mt-1 p-2 w-full border bg-opacity-100 rounded-md bg-gray-900 text-gray-300 focus:outline-none focus:ring focus:border-blue-500 transition-all duration-300"
                            placeholder="Enter class"
                        />
                    </div>
                    <button
                        type="submit"
                        className="bg-black text-white p-2 rounded-md hover:bg-white hover:text-black transition duration-300 focus:outline-none focus:ring focus:border-white bg-opacity-0"
                    >
                        Register
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Register;
