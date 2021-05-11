let positionCode = window.location.href.indexOf("code=") + 5;
let endPositionCode = window.location.href.indexOf("&scope");

let code = window.location.href.slice(positionCode, endPositionCode);

if (positionCode != -1) {
    authorization()
}

function authorization() {
    let AuthorizationLink = 'https://www.strava.com/oauth/token?client_id=64739&client_secret=b2cb9eb6369b18599722fcfe631d11d7f00ec151&code=${code}&grant_type=authorization_code';
    fetch(AuthorizationLink, {
        method: 'POST'
    })
    .then((data) => data.json())
    .then((data) => {
        localStorage.access_token = data.access_token;
        localStorage.refresh_token = data.refresh_token;
        console.log(code)
    })
        
}


