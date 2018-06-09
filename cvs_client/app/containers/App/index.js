/**
 *
 * App
 *
 * This component is the skeleton around the actual pages, and should only
 * contain code that should be seen on all pages. (e.g. navigation bar)
 */

import React from 'react';
import { connect } from 'react-redux';
import GrommetApp from 'grommet/components/App';
import Title from 'grommet/components/Title';
import withProgressBar from 'components/ProgressBar';
import CustomHeader from '../CustomHeader'

export function App(props) {
  return (
    <GrommetApp style={{width: '100%', margin: 0, padding: 0, maxWidth: 'none'}}>
      <CustomHeader/>
      {React.Children.toArray(props.children)}
    </GrommetApp>
  );
}

export default App;
