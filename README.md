# Hidden text using opencv

<ul>Requirements
    <li>A device with internal webcam</li>
    <li>Flask Framework 1.1.2</li>
    <li>Python 3.8.5 </li>
    <li>Anaconda 64-bit</li>
</ul>
<ol>How to run the project
    <li>Download the code and extract it in a folder</li>
    <li>Run the anaconda command prompt</li>
    <li>Change your working directory to the folder(where you've extracted)</li>
    <li>Set the FLASK_APP environment variable to "code.py". Command =  set FLASK_APP=code.py</li>
    <li>Next, run the development server using run command. Command = flask run</li>
    <li>Finally, open your browser and go to http://127.0.0.1:5000/ in order to run the project</li>
</ol>

<ul>About the project
    <li>The project is an basic implementation of image processing OpenCV using changing colourspaces</li>
    <li>Convert BGR image to HSV and use this to extract a colored object. In HSV it is more easier to represent a color than RGB color-space. In this project, we will try to extract a yellow colored object.</li>
    <li>Initially, user is given with a UI with a button, once the user clicks on the button, the webpage is redirected to another page where webcam is initiated.</li>
    <li>In this webpage, the user is provided with the frame where live webcam video is shown and two buttons, 1)Retake the picture and 2) Confirm the picture </li>
    <li>The second user clicks on "Retake the picture" button, the user is redirected to homepage where a button is provided to start the camera</li>
    <li>The second user clicks on "Confirm the picture", a new page is displayed where the hidden text is revealed</li>
    
</ul>

I have also attached a video of the output.

If you have any doubts and/or facing problems while running the code, please let me know in the discussion page or you can mail me - rachanaangara1@gmail.com for prompt reply.
Please make sure your subject contains "git tic-tac-toe-using-minimax-algorithm".

