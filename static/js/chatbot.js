const chatButton = document.getElementById("chat-button");
const chatContainer = document.getElementById("chatContainer");
const minimizeButton = document.getElementById("minimize-button");
const chatInput = document.getElementById("chat-input");
const chatMessages = document.getElementById("conversation-scroll"); 
const sendButton = document.getElementById("SentButton");
const quickMessage = document.getElementsByClassName('sentText');

if (chatButton) {
    chatButton.addEventListener("click", function () {
        if (chatContainer) {
            chatContainer.classList.add("open");
            chatButton.classList.add("clicked");
        }
    });
}

if (minimizeButton) {
    minimizeButton.addEventListener("click", function () {
        if (chatContainer) {
            chatContainer.classList.remove("open");
            chatButton.classList.remove("clicked");
        }
    });
}

function createMessage(message, isUser = true) {
    const newMessage = document.createElement('div');
    newMessage.classList.add(isUser ? 'sentText' : 'botText');
    newMessage.textContent = message;
    chatMessages.appendChild(newMessage);
    return newMessage;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// function chatbotResponse(message) {
//     $.ajax({
//         url: '/chat_bot/',
//         method: 'POST',
//         data: {
//             'message': message,
//             'csrfmiddlewaretoken': getCookie('csrftoken'),
//         },
//         success: function(data) {
//             const responseMessage = data.message;
//             const quickQuestions = data.quickQuestions;
//             createMessage(responseMessage, false).scrollIntoView();

//             if (quickQuestions && quickQuestions.length > 0) {
//                 quickQuestions.forEach((question, index) => {
//                     const quickQuestionsContainer = document.createElement('div');
//                     quickQuestionsContainer.classList.add('botText', 'botText-' + index);
//                     quickQuestionsContainer.style.color = 'blue'; 
//                     const quickQuestionButton = document.createElement('button');
//                     quickQuestionButton.classList.add('botText-button');
//                     quickQuestionButton.textContent = question;
//                     quickQuestionButton.addEventListener('click', function() {
//                         createMessage(question, true).scrollIntoView();
//                     });

//                     quickQuestionsContainer.appendChild(quickQuestionButton);

//                     chatMessages.appendChild(quickQuestionsContainer);
//                 });
//             }
//         }
//     });
// }


function chatbotResponse(message, selectedQuickQuestion) {
    $.ajax({
        url: '/chat_bot/',
        method: 'POST',
        data: {
            'message': message,
            'selectedQuickQuestion': selectedQuickQuestion, 
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        },
        success: function(data) {
            const responseMessage = data.message;
            const quickQuestions = data.quickQuestions;
            createMessage(responseMessage, false).scrollIntoView();

            if (quickQuestions && quickQuestions.length > 0) {
                quickQuestions.forEach((question, index) => {
                    const quickQuestionsContainer = document.createElement('div');
                    quickQuestionsContainer.classList.add('botText', 'botText-' + index);
                    quickQuestionsContainer.style.color = 'blue'; 
                    const quickQuestionButton = document.createElement('button');
                    quickQuestionButton.classList.add('botText-button');
                    quickQuestionButton.textContent = question;
                    quickQuestionButton.addEventListener('click', function() {
                        sendSelectedQuestion(message, question); 
                    });

                    quickQuestionsContainer.appendChild(quickQuestionButton);

                    chatMessages.appendChild(quickQuestionsContainer);
                });
            }
        }
    });
}

function sendSelectedQuestion(message, selectedQuestion) {
    console.log(selectedQuestion);
    $.ajax({
        url: '/chat_bot/',
        method: 'POST',
        data: {
            'message': message,
            'selectedQuestion': selectedQuestion, 
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        },
        success: function(data) {
            const responseMessage = data.message;
            const quickQuestions = data.quickQuestions;
            createMessage(responseMessage, false).scrollIntoView();

            if (quickQuestions && quickQuestions.length > 0) {
                quickQuestions.forEach((question, index) => {
                    const quickQuestionsContainer = document.createElement('div');
                    quickQuestionsContainer.classList.add('botText', 'botText-' + index);
                    quickQuestionsContainer.style.color = 'blue'; 
                    const quickQuestionButton = document.createElement('button');
                    quickQuestionButton.classList.add('botText-button');
                    quickQuestionButton.textContent = question;
                    quickQuestionButton.addEventListener('click', function() {
                        sendSelectedQuestion(message, question); 
                    });

                    quickQuestionsContainer.appendChild(quickQuestionButton);

                    chatMessages.appendChild(quickQuestionsContainer);
                });
            }
        }
    });
}





sendButton.addEventListener("click", function () {
    const message = chatInput.value.trim();
    if (message) {
        createMessage(message, true).scrollIntoView();
        chatInput.value = '';
        chatbotResponse(message);
    }
});

chatInput.addEventListener("keypress", function (event) {
    if (event.keyCode === 13 && !event.shiftKey) {
        event.preventDefault();
        const message = chatInput.value.trim();
        if (message) {
            createMessage(message, true).scrollIntoView();
            chatInput.value = '';
            chatbotResponse(message);
        }
    }
});

chatInput.addEventListener("input", function (event) {
    if (event.target.value) {
        sendButton.classList.add("svgsent");
    } else {
        sendButton.classList.remove("svgsent");
    }
});

function shakeButton() {
    const button = document.getElementById("button-body");
    if (button) {
        button.classList.add("shake");
        setTimeout(() => {
            button.classList.remove("shake");
        }, 500); 
    }
}

setInterval(shakeButton, 5000);

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(shakeButton, 500); 
});



// const chatButton = document.getElementById("chat-button");
// const chatContainer = document.getElementById("chatContainer");
// const minimizeButton = document.getElementById("minimize-button");
// const chatInput = document.getElementById("chat-input");
// const chatMessages = document.getElementById("conversation-scroll");
// const sendButton = document.getElementById("send-button");

// if (chatButton) {
//     chatButton.addEventListener("click", function () {
//         if (chatContainer) {
//             chatContainer.classList.add("open");
//             chatButton.classList.add("clicked");
//         }
//     });
// }

// if (minimizeButton) {
//     minimizeButton.addEventListener("click", function () {
//         if (chatContainer) {
//             chatContainer.classList.remove("open");
//             chatButton.classList.remove("clicked");
//         }
//     });
// }

// function createMessage(message, isUser = true) {
//     const newMessage = document.createElement('div');
//     newMessage.classList.add(isUser ? 'sentText' : 'botText');
//     newMessage.textContent = message;
//     chatMessages.appendChild(newMessage);
//     return newMessage;
// }

// function chatbotResponse(message) {
//     $.ajax({
//         url: '/chat_bot/',
//         method: 'POST',
//         data: {
//             'message': message,
//             'csrfmiddlewaretoken': getCookie('csrftoken'),
//         },
//         success: function(data) {
//             const responseMessage = data.message;
//             const quickQuestions = data.quickQuestions;

//             createMessage(responseMessage, false).scrollIntoView();

//             if (quickQuestions && quickQuestions.length > 0) {
//                 const quickQuestionsContainer = document.createElement('div');
//                 quickQuestionsContainer.classList.add('quick-questions');

//                 quickQuestions.forEach(question => {
//                     const quickQuestionButton = document.createElement('button');
//                     quickQuestionButton.classList.add('quick-question-button');
//                     quickQuestionButton.textContent = question;
//                     quickQuestionButton.addEventListener('click', function() {
//                         createMessage(question, true).scrollIntoView();
//                     });

//                     quickQuestionsContainer.appendChild(quickQuestionButton);
//                 });

//                 chatMessages.appendChild(quickQuestionsContainer);
//             }
//         }
//     });
// }

// sendButton.addEventListener("click", function () {
//     const message = chatInput.value.trim();
//     if (message) {
//         createMessage(message, true).scrollIntoView();
//         chatInput.value = '';
//         chatbotResponse(message);
//     }
// });

// chatInput.addEventListener("keypress", function (event) {
//     if (event.keyCode === 13 && !event.shiftKey) {
//         event.preventDefault();
//         const message = chatInput.value.trim();
//         if (message) {
//             createMessage(message, true).scrollIntoView();
//             chatInput.value = '';
//             chatbotResponse(message);
//         }
//     }
// });

// chatInput.addEventListener("input", function (event) {
//     if (event.target.value) {
//         sendButton.classList.add("svgsent");
//     } else {
//         sendButton.classList.remove("svgsent");
//     }
// });

// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// function shakeButton() {
//     const button = document.getElementById("chat-button");
//     if (button) {
//         button.classList.add("shake");
//         setTimeout(() => {
//             button.classList.remove("shake");
//         }, 500); 
//     }
// }

// setInterval(shakeButton, 5000);

// document.addEventListener("DOMContentLoaded", () => {
//     setTimeout(shakeButton, 500); 
// });
