/**
 * Created by Administrator on 2016/5/10.
 */

var _host_address = 'http://127.0.0.1:8000';
var _ws_address = 'ws://127.0.0.1:8000/';
var _access_token = '';
var _uid = '';
var _msgBuffer = {};

function getUid() {
    return _uid;
}

function setUid(uid) {
    _uid = uid;
}

function getToken() {
    return _access_token;
}

function setToken(token) {
    _access_token = token;
}

function request(options) {
    options = options || {};
    var params = options.params || {};
    $.ajax({
        url : options.url,
        type: 'POST',
        data: params,
        datatype: 'json',
        success: function(ret) {
            var success = options.success;
            var error = options.error;
            if (!!ret["success"]) {
                if (success != null)
                    success.apply(this, [ret.data]);
            } else {
                if (error != null)
                    error.apply(this, [ret.message]);
            }
        }
    })
}

function addQueryParams(url, obj) {
         var key,
         joinChar = (url.indexOf('?') === -1) ? '?' : '&',
         arrParams = [],
         strParams = '';
         for (key in obj) {
             arrParams[arrParams.length] = '&' + key + '=' + obj[key];
         }
         strParams = arrParams.join('').substring(1);
          return url + joinChar + encodeURIComponent(strParams);
}

function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = decodeURIComponent(window.location.search.substr(1)).match(reg);
    if (r != null) return unescape(r[2]); return null;
}