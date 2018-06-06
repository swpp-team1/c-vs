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
import { requestProductDetail, requestRelatedProducts, postRequestComment, getRequestComment } from './actions'
import Image from 'grommet/components/Image'
import Heading from 'grommet/components/Heading'
import Form from 'grommet/components/Form'
import FormField from 'grommet/components/FormField'
import TextInput from 'grommet/components/TextInput'
import Tiles from 'grommet/components/Tiles'
import Tile from 'grommet/components/Tile'
import Card from 'grommet/components/Card'
import Anchor from 'grommet/components/Anchor'
import List from 'grommet/components/List'
import ListItem from 'grommet/components/ListItem'
import RadioButton from 'grommet/components/RadioButton'


const manufacturer = {'CU': 'CU', 'GS': 'GS25', 'SE': 'SEVEN ELEVEN'}
export class ProductDetail extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor() {
    super()
    this.state = {
      relatedRequestDone: false,
      rating: null,
    }
  }
  componentWillMount() {
    this.props.requestProductDetail(this.props.params.id)
    this.props.getRequestComment(this.props.params.id)
  }
  componentWillReceiveProps(nextProps) {
    if (nextProps.productDetail && !nextProps.relatedProducts) {
      if (nextProps.productDetail.small_category || nextProps.productDetail.large_category) {
        nextProps.requestRelatedProducts(nextProps.productDetail.small_category, nextProps.productDetail.large_category)
      }
    }
    if(nextProps.relatedProducts) {
      this.setState({relatedRequestDone: true})
    }
  }

  render() {
    const productDetail = this.props.productDetail ? this.props.productDetail : ''
    const relatedProducts = this.props.relatedProducts ? this.props.relatedProducts.results: []
    const relatedProductsList = (relatedProducts.filter((obj) => (obj.manufacturer !== productDetail.manufacturer && obj.name !== productDetail.name)).concat(relatedProducts.filter((obj) => (obj.manufacturer === productDetail.manufacturer && obj.name !== productDetail.name))))
    console.log(relatedProductsList)

    let relatedCard;
    if(relatedProducts === undefined) {
      relatedCard = (<p>NO RESULT</p>);
    }
    else{
      console.log(relatedProductsList)
      relatedCard = relatedProducts.map((object, index) => {
        if(object.id === this.props.params.id) return;
        else return (<Tile pad='medium' key={index}><Card colorIndex = 'light-1' textSize = 'small' thumbnail = {<Image src={object.image} />} label={object.manufacturer} heading = {object.name} key = {index} onClick={() => {this.props.router.push(`/productDetail/${object.id}`); location.reload();}}/></Tile>);
    })
  }


    return (
      <div>
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
                {
                  productDetail.rating ?
                    <h3 style={{marginBottom: '0'}}>{productDetail.rating}</h3> :
                    <h3 style={{marginBottom: '0'}}>평점이 매겨지지 않았습니다.</h3>
                }
              </div>
            </div>
          </div>
        </div>
        {
          (this.state && this.state.relatedRequestDone || (productDetail !== '' && !(productDetail.small_category || productDetail.large_category))) ? <h3>{relatedProducts.length === 0 ? '인기 상품' : '유사 상품'}</h3> : <div/>
        }
        <Tiles fill={true}>{relatedCard}</Tiles>
        <div style={{display: 'flex', justifyContent:'center', width: '100%'}}>
          <Form style={{display: 'flex', flexDirection: 'column', alignItems: 'center', border: '1px solid rgba(0, 0, 0, 0.15)', padding: '10px', width: '80%'}}>
            <FormField label='짧은 상품평' style={{border: '0px', borderBottom: '1px solid rgba(0,0,0,0.15)'}}>
              <TextInput id='comment-input'/>
            </FormField>
            <div style={{display: 'flex', flexDirection: 'row', justifyContent: 'center', margin: '20px 0px 10px 48px'}}>
              <RadioButton checked={this.state.rating >= 1} onChange={() => this.setState({rating: 1})}/>
              <RadioButton checked={this.state.rating >= 2} onChange={() => this.setState({rating: 2})}/>
              <RadioButton checked={this.state.rating >= 3} onChange={() => this.setState({rating: 3})}/>
              <RadioButton checked={this.state.rating >= 4} onChange={() => this.setState({rating: 4})}/>
              <RadioButton checked={this.state.rating >= 5} onChange={() => this.setState({rating: 5})}/>
            </div>
            <div style={{width: '100%', display: 'flex', flexDirection: 'row', justifyContent: 'flex-end'}}>
              <Anchor
                label='등록'
                disabled={!this.props.loginResult}
                onClick={() => {
                  if(this.props.loginResult)
                    this.props.postRequestComment(document.getElementById('comment-input').value, this.props.params.id, this.state.rating)
                }}
              />
            </div>
          </Form>
        </div>
        <List>
          {
            this.props.commentList  && this.props.commentList.map((comment) => {
              return (
                <ListItem>
                  <span>{comment.content}</span>
                </ListItem>
              )
            })
          }
        </List>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return ({
    productDetail: state.get('productDetail').toJS().productDetail,
    loginResult: state.get('global').toJS().loginResult,
    relatedProducts: state.get('productDetail').toJS().relatedProducts,
    commentList: state.get('productDetail').toJS().commentList,
  })}

function mapDispatchToProps(dispatch) {
  return {
    requestProductDetail: (id) => dispatch(requestProductDetail(id)),
    requestRelatedProducts: (smallCategory, largeCategory) => dispatch(requestRelatedProducts(smallCategory, largeCategory)),
    postRequestComment: (content, product, rating) => dispatch(postRequestComment(content, product, rating)),
    getRequestComment: (id) => dispatch(getRequestComment(id))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ProductDetail);
