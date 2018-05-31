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
import CustomHeader from '../../components/CustomHeader'


export class ProductAll extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <div>
        <Article>
        <CustomHeader/>
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
      </div>

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
