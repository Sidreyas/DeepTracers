import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import Solutions from './pages/Solutions';
import UseCases from './pages/UseCases';
import Resources from './pages/Resources';
import Technology from './pages/Technology';
import Contact from './pages/Contact';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/solutions" component={Solutions} />
          <Route path="/use-cases" component={UseCases} />
          <Route path="/resources" component={Resources} />
          <Route path="/technology" component={Technology} />
          <Route path="/contact" component={Contact} />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
