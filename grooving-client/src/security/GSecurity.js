const ROLES = ['ANONYMOUS', 'ARTIST', 'CUSTOMER'];
const CUSTOMER_ACCOUNT_CREDENTIALS = 'pug';
const ARTIST_ACCOUNT_CREDENTIALS = 'rosalia';

class GSecurity {

    constructor(username = 'anonymous', role = 'anonymous', token = ''){
      
      this._username = username;
      
      if (role != undefined && ROLES.includes(role.toUpperCase())){
        this._role = role;
      }

      this._token = token;

    }

    getRole(){
        return this._role;
    }
  
    authenticate(username, password){
      // Finish with API
      if(username === password){
          if(username == CUSTOMER_ACCOUNT_CREDENTIALS){
              this._username = username;
              this._token = 'ABC';
              this._role = 'CUSTOMER';
          }else if (username == ARTIST_ACCOUNT_CREDENTIALS){
              this._username = username;
              this._token = 'ABC';
              this._role = 'ARTIST';
          }else{
              return false
          }

          return true;
      }

      return false;
    }

    deauthenticate(){
        this._username = 'anonymous';
        this._role = 'ANONYMOUS';
        this._token = '';
    }

    isAuthenticated(){
        return this._token != undefined && this._token.length > 0;
    }

    isAnonymous(){
        return this._token != undefined && this._token.length == 0;
    }
    
    hasRole(role){

        if(role != undefined && ROLES.includes(role.toUpperCase())){
            return this._role.toUpperCase() === role.toUpperCase();
        }
        else
            return false;
    }

    setRole(role){

        if(role != undefined && ROLES.includes(role.toUpperCase())){
            this._role = role;
            return true;
        }
        else
            return false;
    }

  }
  
  const instance = new GSecurity();

  console.log('hola');
  export default instance;