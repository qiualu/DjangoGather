// 封装弹窗layer组件等
var common_ops = {
  alert:function( msg ,cb ){
      layer.alert( msg,{
          yes:function( index ){
              if( typeof cb == "function" ){
                  cb();
              }
              layer.close( index );
          }
      });
  },
  confirm:function( msg,callback ){
      callback = ( callback != undefined )?callback: { 'ok':null, 'cancel':null };
      layer.confirm( msg , {
          btn: ['确定','取消'] //按钮
      }, function( index ){
          //确定事件
          if( typeof callback.ok == "function" ){
              callback.ok();
          }
          layer.close( index );
      }, function( index ){
          //取消事件
          if( typeof callback.cancel == "function" ){
              callback.cancel();
          }
          layer.close( index );
      });
  },
  tip:function( msg,target ){
      layer.tips( msg, target, {
          tips: [ 3, '#e5004f']
      });
      $('html, body').animate({
          scrollTop: target.offset().top - 10
      }, 100);
  }
};

// 功能
$(document).ready(function() {
  var chatBtn = $('#chatBtn');
  var chatInput = $('#chatInput');
  var chatWindow = $('#chatWindow');

  // 存储对话信息,实现连续对话
  var messages = []

  // 转义html代码，防止在浏览器渲染
  function escapeHtml(html) {
    var text = document.createTextNode(html);
    var div = document.createElement('div');
    div.appendChild(text);
    return div.innerHTML;
  }

  /// 添加消息到窗口
  function addMessage(message,imgName) {
    $(".answer .tips").css({"display":"none"});    // 打赏卡隐藏
    chatInput.val('');
    var escapedMessage;
    if (imgName == "avatar.png"){
      escapedMessage= escapeHtml(message);  // 对请求message进行转义，防止输入的是html而被浏览器渲染
    }else if(imgName == "chatgpt.png"){
      escapedMessage= marked(message);  // 使用marked.js对响应message的markdown格式转换为html
    }
    console.log("YL imgName5 : ",imgName)
    console.log("YL escapedMessage5 : ",escapedMessage)
    console.log("YL csrftoken : ",getCookie('csrftoken'))
    var messageElement = $('<div class="row message-bubble"><img class="chat-icon" src="/static/images/' + imgName + '"><div class="message-text">' +  escapedMessage + '</div></div>');
    chatWindow.append(messageElement);
    chatWindow.animate({ scrollTop: chatWindow.prop('scrollHeight') }, 500);
  }

  function addMessageStream(messageStream) {


    var messageBubbles = document.querySelectorAll('.message-bubble');
    var lastMessageText = messageBubbles[messageBubbles.length - 1].querySelector('.message-text');

    var escapedMessage;
//        var divElement = document.createElement('div');
//        divElement.innerHTML = escapeHtml(messageStream); // 对文本进行转义
    escapedMessage= escapeHtml(messageStream);
//        divElement.style.display = 'inline-block';
//    lastMessageText.innerHTML = lastMessageText.innerHTML + escapedMessage; // 清空消息气泡中的内容
    lastMessageText.innerHTML = escapedMessage; // 清空消息气泡中的内容
    //lastMessageText.appendChild(divElement); // 直接插入到最后一个消息气泡中的 .message-text 元素中

    lastMessageText.animate({ scrollTop: chatWindow.prop('scrollHeight') }, 500);
}


  // 发送消息到服务器
  // 请求失败不用转义html
  function addFailMessage(message) {
    $(".answer .tips").css({"display":"none"});      // 打赏卡隐藏
    chatInput.val('');
    var messageElement = $('<div class="row message-bubble"><img class="chat-icon" src="/static/images/chatgpt.png"><div class="message-text error">' +  message + '</div></div>');
    chatWindow.append(messageElement);
    chatWindow.animate({ scrollTop: chatWindow.prop('scrollHeight') }, 500);
  }

  chatBtn.click(function() {

    // ajax上传数据
    var data = {}

    // 判断是否使用自己的api key
    if ($(".key .ipt-1").prop("checked")){
      var apiKey = $(".key .ipt-2").val();
      if (apiKey.length < 20 ){
          common_ops.alert("请输入正确的 api key ！",function(){
            chatInput.val('');
            // 重新绑定键盘事件
            chatInput.on("keydown",handleEnter);
          })
          return
      }else{
        data["apiKey"] = apiKey
      }
    }

    var message = chatInput.val();
    if (message.length == 0){
      common_ops.alert("请输入内容！",function(){
        chatInput.val('');
        // 重新绑定键盘事件
        chatInput.on("keydown",handleEnter);
      })
      return
    }

    addMessage(message,"avatar.png");

    // 将用户消息保存到数组
    messages.push({"role": "user", "content": message})

    // 收到回复前让按钮不可点击
    chatBtn.attr('disabled',true)
    console.log("YL messages5512 : ",messages)
    console.log("YL messages5333 : ",message)

    data["prompt"] = message // JSON.stringify(messages)
    data["id"] = id


    var messageStream = ""
    addMessage(messageStream,"chatgpt.png");


    var setTime = 1

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/gpt/chat/', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 3) {
            // 当readyState为3时，表示已经接收到了部分的返回数据
//             console.log("ajax : ",xhr.responseText);
            //messageStream += xhr.responseText;
            addMessageStream(xhr.responseText)
//            addMessageStream(messageStream);
//            addMessageStream(messageStream,"chatgpt.png");
            // 这里可以将接收到的数据进行处理
        } else if (xhr.readyState === 4) {
            // 当readyState为4时，表示已经接收到了所有的返回数据
//            console.log(xhr.responseText);
            // 这里可以对最终的数据进行处理
            // 收到回复，让按钮可点击
          chatBtn.attr('disabled',false)
          // 重新绑定键盘事件
          chatInput.on("keydown",handleEnter);
        }
    };
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // 添加CSRF token
    var data = {
        "prompt": message,
        "id": id
    };

    xhr.send(JSON.stringify(data)); // 发送JSON格式的数据

  });



    function escapeHtml(text) {
      var map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
      };
      return text.replace(/[&<>"']/g, function(m) { return map[m]; });
    }


  // Enter键盘事件
  function handleEnter(e){
    if (e.keyCode==13){
      chatBtn.click();
      e.preventDefault();  //避免回车换行
    }
  }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

  // 绑定Enter键盘事件
  chatInput.on("keydown",handleEnter);
});