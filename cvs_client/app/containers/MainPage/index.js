/*
 *
 * MainPage
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { FormattedMessage } from 'react-intl';
import { createStructuredSelector } from 'reselect';
import makeSelectMainPage from './selectors';
import messages from './messages';
import App from 'grommet/components/App';
import Header from 'grommet/components/Header';
import Title from 'grommet/components/Title';
import Article from 'grommet/components/Article';
import Button from 'grommet/components/Button';
import Section from 'grommet/components/Section';
import User from 'grommet/components/icons/base/User';
import Search from 'grommet/components/Search';
import Footer from 'grommet/components/Footer';
import Heading from 'grommet/components/Heading';
import Hero from 'grommet/components/Hero';
import Image from 'grommet/components/Image';
import Box from 'grommet/components/Box';
import Tiles from 'grommet/components/Tiles';
import Tile from 'grommet/components/Tile';
import Card from 'grommet/components/Card';
import Anchor from 'grommet/components/Anchor';

// How to load image?


export class MainPage extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <App>
        <Article>
          <Header style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0px 15px'}}>
            <div style={{display: 'flex', flexDirection: 'row', alignItems: 'center'}}>
              <Title>C:VS</Title>
              <Button plain={true} label='제품' href='#'/>
              <Button plain={true} label='레시피' href='#'/>
            </div>
            <div>
              <Button plain={true} icon={<User size='small'/>} label='로그인' href='#'/>
            </div>
          </Header>
          {/**/}
          <Hero background={<Image src='https://images.pexels.com/photos/811108/pexels-photo-811108.jpeg' fit='cover' full={true} />}
            backgroundColorIndex='dark' size='small'>
            <Box direction='row' justify='center' align='center'>
              {/* <Box basis='1/2' align='end'pad='medium' /> */}
              <Box basis='1/2' align='start' pad='medium'>
              <Section style={{alignItems: 'center', justifyContent: 'center', height: 300}}>
              <Heading margin='none' strong = {true} tag = 'h2'>제품 및 레시피 검색</Heading>
                {/* <Title>제품 및 레시피 검색</Title> */}
                <Search style={{width: '700px', margin: '20px 0px'}} inline={true} placeHolder='검색' />
              </Section>
                
                
              </Box>
              
            </Box>
          </Hero>
          {/* <Section style={{alignItems: 'center', justifyContent: 'center', height: 300, backgroundColor: '#f6f6f6'}}>
            <Title>제품 및 레시피 검색</Title>
            <Search style={{width: '700px', margin: '20px 0px'}} inline={true} placeHolder='검색'/>
          </Section> */}

          <Section colorIndex='light-2'>
          <Heading tag = 'h2' align = 'start'>인기 제품</Heading>
          <Tiles fill={false} flush={false} >
          <Tile>
          <Card thumbnail='http://cdn2.bgfretail.com/bgfbrand/files/product/5D8998FE3B78430B99641CCA0C3F3506.jpg'
                label='Sample Label'
                heading='Sample Heading'
                description='Sample description providing more details.'
                link={<Anchor href=''
                label='Sample anchor' />}
                colorIndex='light-1' />
          </Tile>
          </Tiles>
          </Section>


          <Footer style={{justifyContent: 'center'}}>
            <Heading style={{fontSize: 15}}>@ 2018 C:VS</Heading>
          </Footer>
        </Article>
      </App>
    );
  }
}

MainPage.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

const mapStateToProps = createStructuredSelector({
  MainPage: makeSelectMainPage(),
});

function mapDispatchToProps(dispatch) {
  return {
    dispatch,
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(MainPage);
