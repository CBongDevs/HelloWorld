import React from 'react';
import logo from './logo.svg';
import './App.css';

interface AppState {
  status: string;
}

class App extends React.Component<{}, AppState> {

  constructor(props: any) {
    super(props);
    this.state = { status: '' };
  }

  async buttonClick() {
    let request = await fetch('/api/ping');
    let json = await request.json();
    this.setState({
      'status': json['time']
    });
  }

  render(): JSX.Element {
    return (
    <div onClick={this.buttonClick.bind(this)} className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p key={Date.now()} id='status'>
          {this.state.status}
        </p>
      </header>
    </div>)
  }
}

export default App;
