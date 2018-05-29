/*
 *
 * ProductAll
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Helmet from 'react-helmet';
import { FormattedMessage } from 'react-intl';
import { createStructuredSelector } from 'reselect';
import makeSelectProductAll from './selectors';
import messages from './messages';
import App from 'grommet/components/App';
import Card from "grommet/components/Card";
import Tiles from 'grommet/components/Tiles';
import Tile from 'grommet/components/Tile';
import Header from 'grommet/components/Header';
import Button from 'grommet/components/Button';
import Title from 'grommet/components/Title';
import User from 'grommet/components/icons/base/User';
import Section from 'grommet/components/Section';
import Article from 'grommet/components/Article';
import { Redirect } from 'react-router/lib';


export class ProductAll extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <App>
        <Article>
        <Header style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0px 15px'}}>
            <div style={{display: 'flex', flexDirection: 'row', alignItems: 'center'}}>
              <Title onClick={<Redirect to=""/>}>C:VS</Title>
              <Button plain={true} label='제품' href='productAll'/>
              <Button plain={true} label='레시피' href='#'/>
            </div>
            <div>
              <Button plain={true} icon={<User size='small'/>} label='로그인' href='#'/>
            </div>
          </Header>
      <Section colorIndex='light-2'>
      <Tiles  fill={false} flush={false} >
      <Tile>
      <Card thumbnail='http://cdn2.bgfretail.com/bgfbrand/files/product/5D8998FE3B78430B99641CCA0C3F3506.jpg'
                textSize='small'
                label='Sample Label'
                heading='Sample Heading'
                description='Sample description providing more details.'
                onClick = {() => alert("clicked")}
                // link={<Anchor href=''
                // label='Sample anchor' />}
                colorIndex='light-1' />
      </Tile>
      </Tiles>
      </Section>
      </Article>
      </App>
      
      // <div>
      //   <Helmet
      //     title="ProductAll"
      //     meta={[
      //       { name: 'description', content: 'Description of ProductAll' },
      //     ]}
      //   />
      //   <FormattedMessage {...messages.header} />
      // </div>
    );
  }
}

ProductAll.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

const mapStateToProps = createStructuredSelector({
  ProductAll: makeSelectProductAll(),
});

function mapDispatchToProps(dispatch) {
  return {
    dispatch,
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ProductAll);
