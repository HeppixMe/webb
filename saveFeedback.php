<?php
  $message = $_POST['message']; // incoming message
  file_put_contents('Feedback.log', $message, FILE_APPEND);
  header('Location: /'); // redirect back to the main site