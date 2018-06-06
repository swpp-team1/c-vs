import React from 'react';
import Header from 'grommet/components/Header';
import Title from 'grommet/components/Title';
import Button from 'grommet/components/Button';
import Anchor from 'grommet/components/Anchor';
import User from 'grommet/components/icons/base/User';
import Search from 'grommet/components/icons/base/Search';
import { withRouter } from 'react-router';


class CustomHeader extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <Header style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0px 15px'}}>
        <div style={{display: 'flex', flexDirection: 'row', alignItems: 'center'}}>
          <Title onClick={() => this.props.router.push('/')}>C:VS</Title>
          <Button plain={true} label='제품' href='/productAll'/>
          <Button plain={true} label='레시피' href='/recipeAll'/>
        </div>
        <div>
          <Anchor icon={<Search size='small'/>} label='검색' href='/search' animateIcon={false} style={{margin : '0px 20px'}}/>
          {
            !this.props.loginResult ?
            <Anchor icon={<User size='small'/>} label='로그인' href='/login' animateIcon={false}/> :
              <Anchor icon={<User size='small'/>} label='로그아웃' onClick={() => this.props.loginRequest()} animateIcon={false}/>
          }
        </div>
      </Header>
    );
  }
}

export default withRouter(CustomHeader);
