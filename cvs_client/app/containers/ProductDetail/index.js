/*
 *
 * ProductDetail
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';
import makeSelectProductDetail from './selectors';
import CustomHeader from '../../components/CustomHeader'
import { requestProductDetail } from './actions'
import Image from 'grommet/components/Image'
import Heading from 'grommet/components/Heading'


export class ProductDetail extends React.Component { // eslint-disable-line react/prefer-stateless-function
  componentWillMount() {
    this.props.requestProductDetail(this.props.params.id)
  }
  render() {
    console.log(this.props.ProductDetail.productDetail)
    const productDetail = this.props.ProductDetail.productDetail ? this.props.ProductDetail.productDetail : ''
    return (
      <div>
        <CustomHeader/>
        <div style={{flexDirection: 'row', display: 'flex', padding: '30px'}}>
          <div style={{width: '250px', justifyContent: 'center', display: 'flex'}}>
            <Image fit='contain' size='large' src={productDetail.image}/>
          </div>
          <div style={{padding: '20px 50px'}}>
            <h3>{productDetail.manufacturer}</h3>
            <Heading style={{marginBottom: '100px'}}>{productDetail.name}</Heading>
            <div style={{display: 'flex', flexDirection: 'row'}}>
              <div style={{display: 'flex', flexDirection: 'column', marginRight: '30px'}}>
                <h3 style={{marginBottom: '10px'}}>가격</h3>
                <h3 style={{marginBottom: '0'}}>{productDetail.price}</h3>
              </div>
              <div style={{display: 'flex', flexDirection: 'column'}}>
                <h3 style={{marginBottom: '10px'}}>평점</h3>
                <h3 style={{marginBottom: '0'}}>{productDetail.price}</h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = createStructuredSelector({
  ProductDetail: makeSelectProductDetail(),
});

function mapDispatchToProps(dispatch) {
  return {
    requestProductDetail: (id) => dispatch(requestProductDetail(id))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ProductDetail);
