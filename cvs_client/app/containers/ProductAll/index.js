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
import { getAllProducts } from './actions'
import Image from 'grommet/components/Image'


export class ProductAll extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor(props){
    super(props);
    this.state={
      id: 1
    };
  }

  componentWillMount() {
    this.props.getProductAll(this.state.id)
  }
  render() {

    var allCard;
    if(this.props.ProductAll.productsList == undefined) {
      allCard = (<p>NO AVAILABLE RESULT</p>);
    }
    else{
      console.log(this.props.ProductAll.productsList.results)
      allCard = this.props.ProductAll.productsList.results.map((object, index) => {
      return (<Tile pad='medium' key={index}><Card colorIndex = 'light-1' textSize = 'small' thumbnail = {<Image src={object.image} />} label={object.manufacturer} heading = {object.name} key = {index} onClick={() => this.props.router.push(`/productDetail/${object.id}`)}/></Tile>);
    })
  }

    return (
      <div>
        <Article>
          <Section colorIndex='light-2'>
            <Tiles  fill={true}>
              { allCard }
            </Tiles>
          </Section>
        </Article>
      </div>
    );
  }
}

const mapStateToProps = createStructuredSelector({
  ProductAll: makeSelectProductAll(),
});

function mapDispatchToProps(dispatch) {
  return {
    getProductAll: (id) => dispatch(getAllProducts(id))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ProductAll);
