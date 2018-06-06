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
import { requestProductDetail, requestRelatedProducts } from './actions'
import Image from 'grommet/components/Image'
import Heading from 'grommet/components/Heading'
import Form from 'grommet/components/Form'
import FormField from 'grommet/components/FormField'
import TextInput from 'grommet/components/TextInput'


const manufacturer = {'CU': 'CU', 'GS': 'GS25', 'SE': 'SEVEN ELEVEN'}
export class ProductDetail extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor() {
    super()
    this.state = {
      relatedRequestDone: false
    }
  }
  componentWillMount() {
    this.props.requestProductDetail(this.props.params.id)
  }
  componentWillReceiveProps(nextProps) {
    if (nextProps.productDetail && !nextProps.relatedProducts) {
      if (nextProps.productDetail.small_category || nextProps.productDetail.large_category) {
        nextProps.requestRelatedProducts(nextProps.productDetail.small_category, nextProps.productDetail.large_category)
        console.log('!!!!')
      }
    }
    if(nextProps.relatedProducts) {
      this.setState({relatedRequestDone: true})
    }
  }
  render() {
    const productDetail = this.props.productDetail ? this.props.productDetail : ''
    const relatedProducts = this.props.relatedProducts ? this.props.relatedProducts: []
    const relatedProductsList = (relatedProducts.filter((obj) => (obj.manufacturer !== productDetail.manufacturer && obj.name !== productDetail.name)).concat(relatedProducts.filter((obj) => (obj.manufacturer === productDetail.manufacturer && obj.name !== productDetail.name))))
    console.log(relatedProductsList)
    return (
      <div>
        <CustomHeader/>
        <div style={{flexDirection: 'row', display: 'flex', padding: '30px'}}>
          <div style={{width: '250px', justifyContent: 'center', display: 'flex'}}>
            <Image fit='contain' size='large' src={productDetail.image}/>
          </div>
          <div style={{padding: '20px 50px'}}>
            <h3>{manufacturer[productDetail.manufacturer]}</h3>
            <Heading style={{marginBottom: '100px'}}>{productDetail.name}</Heading>
            <div style={{display: 'flex', flexDirection: 'row'}}>
              <div style={{display: 'flex', flexDirection: 'column', marginRight: '30px'}}>
                <h3 style={{marginBottom: '10px'}}>가격</h3>
                <h3 style={{marginBottom: '0'}}>{'￦ '+productDetail.price}</h3>
              </div>
              <div style={{display: 'flex', flexDirection: 'column'}}>
                <h3 style={{marginBottom: '10px'}}>평점</h3>
                <h3 style={{marginBottom: '0'}}>{productDetail.price}</h3>
              </div>
            </div>
          </div>
        </div>
        {
          (this.state && this.state.relatedRequestDone || (productDetail !== '' && !(productDetail.small_category || productDetail.large_category))) ? <h3>{relatedProducts.length === 0 ? '인기 상품' : '유사 상품'}</h3> : <div/>
        }
        <Form>
          <FormField label='짧은 상품평'>
            <TextInput/>
          </FormField>
        </Form>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return ({
    productDetail: state.get('productDetail').toJS().productDetail,
    relatedProducts: state.get('productDetail').toJS().relatedProducts
  })}

function mapDispatchToProps(dispatch) {
  return {
    requestProductDetail: (id) => dispatch(requestProductDetail(id)),
    requestRelatedProducts: (smallCategory, largeCategory) => dispatch(requestRelatedProducts(smallCategory, largeCategory))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ProductDetail);
