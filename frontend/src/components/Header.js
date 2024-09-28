import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="bg-primary text-white">
      <nav className="container mx-auto px-6 py-3 flex justify-between items-center">
        <Link to="/" className="text-xl font-bold">
          DeepTracers
        </Link>
        <div className="hidden md:flex space-x-4">
          <Link to="/solutions" className="hover:text-gray-300">Solutions</Link>
          <Link to="/use-cases" className="hover:text-gray-300">Use Cases</Link>
          <Link to="/resources" className="hover:text-gray-300">Resources</Link>
          <Link to="/technology" className="hover:text-gray-300">Technology</Link>
          <Link to="/contact" className="hover:text-gray-300">Contact</Link>
          <Link to="/signup" className="hover:text-gray-300">Sign Up</Link>
          <Link to="/signin" className="hover:text-gray-300">Sign In</Link>
        </div>
      </nav>
    </header>
  );
}

export default Header;
