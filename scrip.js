class Chatbox {
    constructor() {
      this.args = {
        openButton: document.querySelector('.chatbox__button'),
        chatBox: document.querySelector('.chatbox__support'),
        sendButton: document.querySelector('.send__button'),
        closeButton: document.querySelector('.chatbox__close-button')
      };
  
      this.state = false;
      this.messages = [];
    }
  
    display() {
      const { openButton, chatBox, sendButton, closeButton } = this.args;
  
      openButton.addEventListener('click', () => this.toggleState(chatBox));
  
      closeButton.addEventListener('click', () => this.toggleState(chatBox));
  
      sendButton.addEventListener('click', () => this.onSendButton(chatBox));
  
      sendButton.addEventListener('click', () => {
    
    let inputValue = document.querySelector('input[type="text"]').value;  // Get the input field value
  
  
  });
  
  
      const node = chatBox.querySelector('input');
      node.addEventListener('keyup', ({ key }) => {
        if (key === 'Enter') {
          this.onSendButton(chatBox);
        }
      });
    }
  
    toggleState(chatbox) {
      this.state = !this.state;
  
      // show or hides the box
      if (this.state) {
        chatbox.classList.add('chatbox--active');
      } else {
        chatbox.classList.remove('chatbox--active');
      }
    }
  
    onSendButton(chatbox) {
      var textField = chatbox.querySelector('input');
      let text1 = textField.value;
      if (text1 === '') {
        return;
      }
  
      let msg1 = { name: 'User', message: text1 };
      this.messages.push(msg1);
  
      fetch('/api/predictt', {
        method: 'POST',
        body: JSON.stringify({ message: text1 }),
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(r => r.json())
        .then(r => {
          let msg2 = { name: 'Assist', message: r.query.answer };
          this.messages.push(msg2);
          this.updateChatText(chatbox);
          textField.value = '';
        })
        .catch(error => {
          console.error('Error:', error);
          this.updateChatText(chatbox);
          textField.value = '';
        });
    }
    
    updateChatText(chatbox) {
    var html = '';
    var messages = this.messages.slice().reverse();
    for (var i = 0; i < messages.length; i++) {
      var item = messages[i];
      var className = 'messages__item';
      if (item.name === "Assist") {
        className += ' messages__item--visitor';
      } else {
        className += ' messages__item--operator';
      }
      if (i > 0 && messages[i-1].name === "User") {
        className += ' replying';
      }
  
      // Split the message into paragraphs
      var paragraphs = item.message.split('\n');
      for (var j = 0; j < paragraphs.length; j++) {
        var paragraph = paragraphs[j];
        var message = paragraph.replace(/(https?:\/\/[^\s]+)|(www\.[^\s]+)/g, '<a href="$&" target="_blank" style="word-wrap: break-word">$&</a>');
  
        // Detect and print points
        const regex = /([a-z]\])|(10\])|(11\])|(12\])/gi;
        message = message.replace(regex, '<br>&bull; ');
  
        const regex2 = /\d+\)\s*/gi;
        const matches = paragraph.matchAll(regex2);
        for (const match of matches) {
          message = message.replace(match[0], '<br>' + match[0]);
        }
  
        html += '<div class="' + className + '">' + message + '</div>';
      }
    }
  
    const chatmessage = chatbox.querySelector('.chatbox__querys .chatbox__messages');
    chatmessage.innerHTML = html;
  }
  
  
    
  
  /* 
  updateChatText(chatbox) {
    var html = '';
    var messages = this.messages.slice().reverse();
    for (var i = 0; i < messages.length; i++) {
      var item = messages[i];
      var className = 'messages__item';
      if (item.name === "Assist") {
        className += ' messages__item--visitor';
      } else {
        className += ' messages__item--operator';
      }
      if (i > 0 && messages[i-1].name === "User") {
        className += ' replying';
      }
  
      // Split the message into paragraphs
      var paragraphs = item.message.split('\n');
      for (var j = 0; j < paragraphs.length; j++) {
        var paragraph = paragraphs[j];
        var message = paragraph.replace(/(https?:\/\/[^\s]+)|(www\.[^\s]+)/g, '<a href="$&" target="_blank">$&</a>');
  
        // Check if the message has points
        var pointsMatch = message.match(/^(?:(?:\s*\d+[a-zA-Z0-9]*\)\s+.+\n?){2,}|(?:.+\n){2,}\s*\d+[a-zA-Z0-9]*\)\s+.+\n?)/gm);
        if (pointsMatch) {
          // Split the message into points
          var points = message.split(/^(?:(?:\s*\d+[a-zA-Z0-9]*\)\s+.+\n?){2,}|(?:.+\n){2,}\s*\d+[a-zA-Z0-9]*\)\s+.+\n?)/gm).slice(1);
          // Add newlines between points
          message = points.join('\n');
          message = message.replace(/(?:\b\d+|[iIvVxX]{1,3})\)[\s]*|[a-z]+\)/g, '<b>$&</b>'); // Add bold to pattern matches
        }
  
        html += '<div class="' + className + '">' + message + '</div>';
      }
    }
  
    const chatmessage = chatbox.querySelector('.chatbox__querys .chatbox__messages');
    chatmessage.innerHTML = html;
  }
  
  */
  
  
  }
  
  const chatbox = new Chatbox();
  chatbox.display();
