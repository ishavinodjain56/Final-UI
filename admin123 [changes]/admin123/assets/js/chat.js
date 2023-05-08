const chatBox = document.querySelector('.chat-box');
const inputMsg = document.querySelector('.message-area textarea');
const sendBtn = document.querySelector('.message-area button');

const responseDict = {
    'hi': 'Hello!',
    'what is your name': 'My name is ChatBot!',
    "hello": "Hi there!",
    "how are you": "I'm doing well, thanks for asking.",
    "bye": "Goodbye!",
    "default": "I'm sorry, I don't understand. Can you please try again?",
    "What is this website about?": "Our website is a platform for parents and children to find resources and support for learning and development.",
    "How do I create an account?": "You can create an account by clicking on the 'Sign Up' button on the homepage and following the instructions.",
    "I forgot my password, what should I do?": "You can reset your password by clicking on the 'Forgot Password' link on the login page and following the instructions.",
    "Where can I find educational resources for my child?": "You can find educational resources by clicking on the 'Resources' tab on the navigation bar.",
    "How can I contact customer support?": "You can contact customer support by clicking on the 'Contact Us' link on the footer of the website and filling out the form.",
    "Is the website safe for children?": "Yes, the website is designed to be a safe and secure platform for children and parents to connect and learn together.",
    "How do I change my profile information?": "You can change your profile information by clicking on the 'My Account' link on the navigation bar and updating your information.",
    "Where can I find parenting tips and advice?": "You can find parenting tips and advice by clicking on the 'Parenting' tab on the navigation bar.",
    "How do I delete my account?": "You can delete your account by contacting customer support and requesting account deletion.",
    "Is there a mobile app for the website?": "Yes, we have a mobile app for iOS and Android devices. You can download it from the App Store or Google Play.",
    "How do I change my email address?": "To change your email address, go to your account settings and update your email information.",
    "How do I cancel my subscription?": "To cancel your subscription, go to your account settings and follow the instructions to cancel.",
    "How do I report inappropriate content on the website?": "To report inappropriate content, click on the report button located next to the content and fill out the form to report the content to the website moderators.",
    "How can I request new content for the website?": "To request new content for the website, go to the contact us page and send a message to the website administrators with your request.",
    "How do I delete my account?": "To delete your account, go to your account settings and follow the instructions to delete your account. Please note that this action is irreversible."
};

/*
function generateResponse(input) {
    const nameRegex = /^I am ([a-zA-Z]+)$/i; // regular expression to match "I am {name}"
    const nameMatch = input.match(nameRegex); // check if input matches the regex

    if (nameMatch) {
        const name = nameMatch[1]; // extract the name from the regex match
        return `Good Name, ${name}!`;
    }
    let response = responseDict[input.toLowerCase()] || responseDict['default'];
    return response;
}
*/
async function generateResponse(message) {
    // Make a POST request to the chatbot API endpoint
    const response = await fetch('http://localhost:5000//api/chatbot', {  //todo: flask-host-url
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    }).then(response => {
        // Handle the response here
        console.log(response);
        return response.json(); // If the response is JSON
    })
        .then(data => {
            // Handle the data here
            console.log(data);
        })
        .catch(error => {
            // Handle errors here
            console.error(error);
        });;

    // Get the response from the server as a JSON object
    const data = await response.json();

    // Return the chat bot's response
    return data.message;
}

function createChatBubble(message, side) {
    let chatLine = document.createElement('div');
    chatLine.classList.add('chat-line');
    let chatBubble = document.createElement('div');
    chatBubble.classList.add('chat');
    chatBubble.classList.add(`chat-${side}`);
    let chatAvatar = document.createElement('div');
    if (side === "left") {
        chatAvatar.classList.add('chat-avatar');
        let avatarLink = document.createElement('a');
        avatarLink.href = 'profile.html';
        avatarLink.classList.add('avatar');
        let avatarImg = document.createElement('img');
        avatarImg.alt = 'John Doe';
        avatarImg.src = 'assets/img/user.jpg';
        avatarImg.classList.add('img-responsive');
        avatarImg.classList.add('img-circle');
        avatarLink.appendChild(avatarImg);
        chatAvatar.appendChild(avatarLink);
        chatBubble.appendChild(chatAvatar);
    }
    let chatBody = document.createElement('div');
    chatBody.classList.add('chat-body');
    let chatMsg = document.createElement('div');
    chatMsg.classList.add('chat-bubble');
    let chatContent = document.createElement('div');
    chatContent.classList.add('chat-content');
    let msgText = document.createElement('p');
    msgText.textContent = message;
    chatContent.appendChild(msgText);
    let msgTime = document.createElement('span');
    msgTime.classList.add('chat-time');
    let time = new Date();
    let hours = time.getHours();
    let minutes = time.getMinutes();
    if (hours < 10) {
        hours = `0${hours}`;
    }
    if (minutes < 10) {
        minutes = `0${minutes}`;
    }
    msgTime.textContent = `${hours}:${minutes} ${hours >= 12 ? 'pm' : 'am'}`;
    chatContent.appendChild(msgTime);
    chatMsg.appendChild(chatContent);
    chatBody.appendChild(chatMsg);
    chatBubble.appendChild(chatBody);
    chatLine.appendChild(chatBubble);
    return chatLine;
}

function sendUserMessage() {
    let message = inputMsg.value.trim();
    if (message === '') {
        return;
    }
    let chatBubble = createChatBubble(message, 'left');
    chatBox.appendChild(chatBubble);
    inputMsg.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
    let response = generateResponse(message);
    setTimeout(() => {
        let chatBubble = createChatBubble(response, 'right');
        chatBox.appendChild(chatBubble);
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 500);
}

sendBtn.addEventListener('click', sendUserMessage);
inputMsg.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendUserMessage();
    }
});

function attachFile() {
    const fileInput = document.getElementById("file-input");
    const file = fileInput.files[0];
    // Open the modal when the link is clicked
    $('.attach-icon').click(function () {
        $('#upload-modal').modal('show');
    });

    // Upload the file when the upload button is clicked
    $('#upload-modal .btn-primary').click(function () {
        var file = $('#file-input')[0].files[0];
        // Do something with the file
        $('#upload-modal').modal('hide');
    });
    console.log(file.name);
}
