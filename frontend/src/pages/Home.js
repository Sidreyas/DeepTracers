import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="container mx-auto px-6 py-8">
      <section className="text-center">
        <h1 className="text-4xl font-bold mb-4">Next-Gen AI Threat Detection</h1>
        <p className="text-xl mb-8">Protect your digital assets with cutting-edge AI technology</p>
        <Link to="/contact" className="btn-primary px-6 py-3 rounded-lg text-lg">Get Started</Link>
      </section>

      <section className="mt-16">
        <h2 className="text-3xl font-semibold mb-6">Our Capabilities</h2>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-2">Advanced Threat Detection</h3>
            <p>Utilize state-of-the-art AI algorithms to identify and mitigate potential threats in real-time.</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-2">Scalable Solutions</h3>
            <p>Our platform grows with your needs, ensuring protection for businesses of all sizes.</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-2">Continuous Learning</h3>
            <p>Our AI models continuously adapt to new threats, providing up-to-date protection.</p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;
