import React, { useState } from "react";

function Upload() {
  const [file, setFile] = useState(null);

  const onChangeHandler = (event) => {
    setFile(event.target.files[0]);
    console.log(event.target.files[0]);
  };

  const onSubmit = () => {
    uploadFile(file);
  };

  const uploadFile = (file) => {
    fetch("/sales", {
      // content-type header should not be specified
      method: "POST",
      body: file,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("this is a success");
        console.log(data);
      })
      .catch((error) => {
        console.log("this is an error");
        console.log(error);
      });
  };

  return (
    <form method="post" action="#" id="#">
      <label>Upload Sales Data</label>
      <input type="file" name="file" onChange={onChangeHandler} />
      {file && (
        <button type="button" onClick={onSubmit}>
          Upload
        </button>
      )}
    </form>
  );
}

export default Upload;
