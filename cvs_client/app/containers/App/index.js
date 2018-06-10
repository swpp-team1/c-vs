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
import Footer from 'grommet/components/Footer'
import Heading from 'grommet/components/Heading'

export function App(props) {
  return (
    <GrommetApp style={{width: '100%', minHeight: '100vh', margin: 0, padding: 0, maxWidth: 'none'}}>
      <CustomHeader/>
      <div style={{minHeight: '100vh'}}>
        {React.Children.toArray(props.children)}
      </div>
      <Footer style={{justifyContent: 'center', bottom: 0, backgroundColor: 'white'}}>
        <Heading style={{fontSize: 15, marginBottom: 0}}>@ 2018 C:VS</Heading>
      </Footer>
    </GrommetApp>
  );
}

export default App;
