# MADI 앱 구축하기

## MADI 앱 생성

GSM 학생 계정을 가지고 있는 사람이라면 누구나 MADI 앱을 만들고 등록 할 수 있습니다. 

아례의 순서에 따라 MADI 앱을 생성해 봅시다.

1. 대시보드에서 앱 추가 버튼을 선택한다

  //**추후 설명 사진 추가 예정**//

2. 앱 정보를 입력한 후 다음으로 버튼을 선택한다

  //**추후 설명 사진 추가 예정**//

3. 사용할 권한을 선택한 후 앱 등록 버튼을 선택한다

  //**추후 설명 사진 추가 예정**//

## MADI 앱을 서비스에 이용하기

그렇다면 이제, 여러분의 서비스에 MADI 앱을 추가해 봅시다.

(  `javascript` 를 사용한 예제입니다. )

1. Nodejs 설정

    Node를 설치하는 단계는 생략하고 아래의 명령어를 통해 필요한 모듈을 설치하자

    ```jsx
    npm install --save axios
    ```

2. 버튼 만들기

    ```html
    // login_button.html

    <button
    type="button"
    onclick="location.href='https://madi.com/oauth/authorize?client_id=<앱 ID>'">
    </button>

    <!-- css로 button을 스타일링 하세요 --!>
    ```

    ```jsx
    // index.js

    const express = require('express');

    const app = express();

    const clientId = '<앱 ID>';
    const clientSecret = '<앱 시크릿 코드>';

    app.get('/', (req, res) => {
      res.render('login_button.html');
    });
    ```

3. MADI로 부터 Token을 발급 받기 위한 `Redirect URI` 작성하기

    ```jsx
    // index.js

    const express = require('express');

    const app = express();

    const clientId = '<앱 ID>';
    const clientSecret = '<앱 시크릿 코드>';

    app.get('/', (req, res) => {
      res.redirect(`https://madi.com/oauth/authorize?client_id=${clientId}`);
    });

    app.listen(3000);
    console.log('App listening on port 3000');
    ```

    위 코드를 실행시키고 `http://localhost:3000` 에 접속하여 버튼을 클릭하면 아래와 같은 화면이 나온다

  //**추후 설명 사진 추가 예정**//

    사용자가 로그인을 한다면, `"http://<Redirect URI>?code=<code>"}` 로 리다이렉트 됩니다. 

    이제 `code`를 통해 토큰을 발급 받기 위한 `Redirect URI`를 구현해 봅시다. 

4. 토큰을 발급받기 위한 `Redirect URI`구현하기

    ```jsx
    // index.js

    const express = require('express');

    const app = express();

    const clientId = '<앱 ID>';
    const clientSecret = '<앱 시크릿 코드>';
    app.listen(3000);
    console.log('App listening on port 3000');
    const axios = require('axios');
    let token = null;

    app.get('/oauth-callback', (req, res) => {
      const body = {
        client_id: clientId,
        client_secret: clientSecret,
        code: req.query.code
      };
      const opts = { headers: { accept: 'application/json' } };
      axios.post(`https://madi.com/oauth/token`, body, opts).
        then(_token => {
          console.log('My token:', _token); // token 확인하기
          token = _token;
        }).
        catch(err => res.status(500).json({ message: err.message }));
    });
    ```

5. 사용자 정보 가져오기

    토큰을 발급받는데 성공했다면 매 요청마다 아래와 같이 `headers`에 `token` 을 넣어 요청을 합니다 

    ```jsx
    app.get('/users', (req, res, next) => {
        const config = {
            headers: {
                Authorization: 'token ' + req.query.token,
                'User-Agent': 'Login-App'
            }
        }
        axios.get('https://madi.com/users', config)
        .then((response) => {
            res.send(response.data[0]);
    				/*
    {
    	"name": "정현문",
    	"stdNo": 2116,
    	"gender": "male",
    	"image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAMFBMVEXFxcX////CwsLGxsb7+/vT09PJycn19fXq6urb29ve3t7w8PDOzs7n5+f5+fnt7e30nlkBAAAFHUlEQVR4nO2dC5qqMAyFMTwUBdz/bq+VYYrKKJCkOfXmXwHna5uTpA+KwnEcx3Ecx3Ecx3Ecx3Ecx3Ecx3Ecx3Ecx3EcA2iO9cdIc5PUdO257y+BU39u66b4HplE3fk6VIcnqmNfl1+gksr6+iIucjl3WYukor7+re6Hoe1y1UhNO3zUd+fUFRmKpOa0Tt6dY5ubRCrOG/QFLk1WGmnt/JxzykcjdZ/jyxJDLlOV2l36AtcsJJb9boG3YcR3DuqODIE3ztYKPkDdmwRmpUToUaSaq++AvRgZMWbOpbQW8hdCAm8ZDugoikzREdCJ2okJPBx6azFLNOwoOgcxojJ98JkaTSJxMpklKrCAKhZGI0drTY/wU5lXoJYibannV9NYy4oozNEAkPHTjop+DTDxVGkIgYJNoyQQJtiIW+EMjGAjm649AjGIaqswcEFQKJ2QPlJbqytki6ZXAAZRJ52J2McaUowzAfs+uFzrYhnzaapphiPWdaJWShqxjqa6kTTQ205TVbsfMa6htL0iYOsXpJrQjHSmCkv1QGPtiHqlYcQ21Gj7fcDU8xOEUuNgSltPzexh+HqFlanCBHZ4OLhCV+gK/3OF6vWvucLv98MUOY2pwu/PS/+D2qJU7pYGbOvDFDW+bbON9p3o3oRxn0bfLgZTgSn6pSfrtr56qLHemtHPTK2319SzGvtjQ9qeb39WgS66Cm073nd0U1PzDdJCO3Gzn6TKpl9Zq7ujGWsQhlA3NwWIMwG9zM08Y/tBrR9VWeczv5CSQuuUNKIUTk23ZJ5RKfVhjnkXotfWIlgX2BSCDYbZR+QTcLhb3dKZDUY2M0d4KWItwhHRah/zsrOgKw4wycwjcgEVcgQDQo23CqSiWEJkFAfod2oE1uIFdA1OsCPqFXYNTjCfb8Ez+iX2x5sKLlVbhtqdDcar9ZevhnbZxoBUD35k23t0d304LYs1ELVbnfFaZ/REJJX9niP8Q19moZGo3m8XR/yBvOnjFfsXcI2c8ZuNo7WMP5HQh6yRGrlmFOJTnyTcT+zRlqPUBI2gTVWNUzUna1ERgecgF4GpNBQ38jGqxVLzQA1A31Rrhk6Yz9QEh/WND0GnuG9huhiTXJkxfAizTHLr6cbJKN6UCU6x/2DTRE1xEeEXi3O0ZUqBN4nJRzHhFB1JPlFTBZlI2kQ8zc3KJ1Le8DIRmFJiknuVS6RK4Ej/JtBfJErDSzOBiY4wJHX6Z1I4v1GUmdCPNirnLLeg3oJLcbX5PcpHNbRvOa1A956QmRPOUXVF+zkaUJynpkYR0bOMJH2nNej1pqyV/aKkz9jr5yj5vrXXz1F5SQLACiMapmierj2ikLyleKdlA/I/2oFxiglxx9B+mHwz0lf34IZQfhDRhlD6bhvgEAoPYooHkTczSIZTLC+cEExsoNKZiGBiY9cCfo/Y/SjIOBMQizWWTe73CMUasJx7jlD+DdKdWUKoY4PRYFtGpO0G1Lx4RaadgTtJhf4fiGqGIwKWCGuGIwKWqP+7IxYCzygjR9IAO5pC7Da9g70TBVpWRNgFBlgT8RV2WxHbKwJMv4BOaEaYaU2K16yZMN/qgV+G7IWIvwyZCxHeDQMsR8wg0DBDDXB5H2EV+hkEGmaoySHQsEJNFoGGFWrAq98JRhUMX1iMMMqLLEIpK5jCbd4vw9nSt/72lewXiN6jmdjfq8Hdknlk92ZwJnbIMMRM7JBhiFlUFoHd1UWaP1QKsPsHA5mkNB+Smn9JqV3wskatnQAAAABJRU5ErkJggg=="
    }
    				*/
        })
        .catch(function(err) {
            console.log(err)
        })
    });
    ```

전체적인 코드

```jsx
// index.js

const express = require('express');
const app = express();
const axios = require('axios');
let token = null;

const clientId = '<앱 ID>';
const clientSecret = '<앱 시크릿 코드>';

// madi 로그인 페이지로 리다이렉트
app.get('/', (req, res) => {
  res.redirect(`https://madi.com/oauth/authorize?client_id=${clientId}`);
});

// code를 url parameter로 받을 redirect uri
// http://<Redirect URI>?code=<code>}
app.get('/oauth-callback', (req, res) => {
  const body = {
    client_id: clientId,
    client_secret: clientSecret,
    code: req.query.code
  };
  const config = { headers: { accept: 'application/json' } };
  axios.post(`https://madi.com/oauth/token`, body, config).
    then(_token => {
      console.log('My token:', _token);
      token = _token;
      res.json({ ok: 1 });
    }).
    catch(err => res.status(500).json({ message: err.message }));
});

// token을 사용해 user 정보를 호출하는 예제
app.get('/users', (req, res, next) => {
    const config = {
        headers: {
            Authorization: 'token ' + req.query.token,
            'User-Agent': 'Login-App'
        }
    }
    axios.get('https://madi.com/users', config)
    .then((response) => {
        res.send(response.data[0]);
				/*
						{
							"name": "정현문",
							"stdNo": 2116,
							"gender": "male",
							"image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAMFBMVEXFxcX////CwsLGxsb7+/vT09PJycn19fXq6urb29ve3t7w8PDOzs7n5+f5+fnt7e30nlkBAAAFHUlEQVR4nO2dC5qqMAyFMTwUBdz/bq+VYYrKKJCkOfXmXwHna5uTpA+KwnEcx3Ecx3Ecx3Ecx3Ecx3Ecx3Ecx3Ecx3EcA2iO9cdIc5PUdO257y+BU39u66b4HplE3fk6VIcnqmNfl1+gksr6+iIucjl3WYukor7+re6Hoe1y1UhNO3zUd+fUFRmKpOa0Tt6dY5ubRCrOG/QFLk1WGmnt/JxzykcjdZ/jyxJDLlOV2l36AtcsJJb9boG3YcR3DuqODIE3ztYKPkDdmwRmpUToUaSaq++AvRgZMWbOpbQW8hdCAm8ZDugoikzREdCJ2okJPBx6azFLNOwoOgcxojJ98JkaTSJxMpklKrCAKhZGI0drTY/wU5lXoJYibannV9NYy4oozNEAkPHTjop+DTDxVGkIgYJNoyQQJtiIW+EMjGAjm649AjGIaqswcEFQKJ2QPlJbqytki6ZXAAZRJ52J2McaUowzAfs+uFzrYhnzaapphiPWdaJWShqxjqa6kTTQ205TVbsfMa6htL0iYOsXpJrQjHSmCkv1QGPtiHqlYcQ21Gj7fcDU8xOEUuNgSltPzexh+HqFlanCBHZ4OLhCV+gK/3OF6vWvucLv98MUOY2pwu/PS/+D2qJU7pYGbOvDFDW+bbON9p3o3oRxn0bfLgZTgSn6pSfrtr56qLHemtHPTK2319SzGvtjQ9qeb39WgS66Cm073nd0U1PzDdJCO3Gzn6TKpl9Zq7ujGWsQhlA3NwWIMwG9zM08Y/tBrR9VWeczv5CSQuuUNKIUTk23ZJ5RKfVhjnkXotfWIlgX2BSCDYbZR+QTcLhb3dKZDUY2M0d4KWItwhHRah/zsrOgKw4wycwjcgEVcgQDQo23CqSiWEJkFAfod2oE1uIFdA1OsCPqFXYNTjCfb8Ez+iX2x5sKLlVbhtqdDcar9ZevhnbZxoBUD35k23t0d304LYs1ELVbnfFaZ/REJJX9niP8Q19moZGo3m8XR/yBvOnjFfsXcI2c8ZuNo7WMP5HQh6yRGrlmFOJTnyTcT+zRlqPUBI2gTVWNUzUna1ERgecgF4GpNBQ38jGqxVLzQA1A31Rrhk6Yz9QEh/WND0GnuG9huhiTXJkxfAizTHLr6cbJKN6UCU6x/2DTRE1xEeEXi3O0ZUqBN4nJRzHhFB1JPlFTBZlI2kQ8zc3KJ1Le8DIRmFJiknuVS6RK4Ej/JtBfJErDSzOBiY4wJHX6Z1I4v1GUmdCPNirnLLeg3oJLcbX5PcpHNbRvOa1A956QmRPOUXVF+zkaUJynpkYR0bOMJH2nNej1pqyV/aKkz9jr5yj5vrXXz1F5SQLACiMapmierj2ikLyleKdlA/I/2oFxiglxx9B+mHwz0lf34IZQfhDRhlD6bhvgEAoPYooHkTczSIZTLC+cEExsoNKZiGBiY9cCfo/Y/SjIOBMQizWWTe73CMUasJx7jlD+DdKdWUKoY4PRYFtGpO0G1Lx4RaadgTtJhf4fiGqGIwKWCGuGIwKWqP+7IxYCzygjR9IAO5pC7Da9g70TBVpWRNgFBlgT8RV2WxHbKwJMv4BOaEaYaU2K16yZMN/qgV+G7IWIvwyZCxHeDQMsR8wg0DBDDXB5H2EV+hkEGmaoySHQsEJNFoGGFWrAq98JRhUMX1iMMMqLLEIpK5jCbd4vw9nSt/72lewXiN6jmdjfq8Hdknlk92ZwJnbIMMRM7JBhiFlUFoHd1UWaP1QKsPsHA5mkNB+Smn9JqV3wskatnQAAAABJRU5ErkJggg=="
						}
				*/
    })
    .catch((err) => {
        console.log(err)
    })
});

app.listen(3000);
console.log('App listening on port 3000');
```
