/**
 *
 * App
 *
 * This component is the skeleton around the actual pages, and should only
 * contain code that should be seen on all pages. (e.g. navigation bar)
 */

import React from 'react';

import GrommetApp from 'grommet/components/App';
import Title from 'grommet/components/Title';
import withProgressBar from 'components/ProgressBar';

export function App(props) {
  return (
    <GrommetApp>
      <Title>Hello World</Title>
      <p>Hello from a Grommet page!</p>
      {React.Children.toArray(props.children)}
    </GrommetApp>
  );
}

App.propTypes = {
  children: React.PropTypes.node,
};

export default withProgressBar(App);
