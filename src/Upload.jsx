import React, { useState, useEffect } from "react";

function Upload() {
  const [showSubmit, setShowSubmit] = useState(false);

  const onChangeHandler = (event) => {
    console.log(event.target.files[0]);
    setShowSubmit(true);
  };

  const onSubmit = () => {
    console.log("submit");
  };

  return (
    <form method="post" action="#" id="#">
      <label>Upload Sales Data</label>
      <input type="file" name="file" onChange={onChangeHandler} />
      {showSubmit && (
        <button type="button" onClick={onSubmit}>
          Upload
        </button>
      )}
    </form>
  );
}

export default Upload;
