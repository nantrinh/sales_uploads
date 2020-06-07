import React, { useState } from "react";

function Upload() {
  const [file, setFile] = useState(null);
  const [uploaded, setUploaded] = useState(false);
  const [num_rows, setNumRows] = useState(null);
  const [revenue, setRevenue] = useState(null);

  const onChangeHandler = (event) => {
    setFile(event.target.files[0]);
    console.log(event.target.files[0]);
  };

  const onSubmit = () => {
    setUploaded(false);
    uploadFile(file);
  };

  const uploadFile = (file) => {
    fetch("http://localhost:5000/sales", {
      // content-type header should not be specified
      method: "POST",
      body: file,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("this is a success");
        console.log(data);
        setNumRows(data["num_rows"]);
        setRevenue(data["revenue"]);
        setUploaded(true);
      })
      .catch((error) => {
        console.log("this is an error");
        console.log(error);
      });
  };

  return (
    <section>
      <form method="post" action="#" id="#">
        <label>Upload Sales Data</label>
        <input type="file" name="file" onChange={onChangeHandler} />
        {file && (
          <button type="button" onClick={onSubmit}>
            Upload
          </button>
        )}
      </form>
      <section>
        {uploaded && (
          <section>
            <p>{num_rows} rows have been uploaded.</p>
            <p>Total Revenue: {revenue}</p>
          </section>
        )}
      </section>
    </section>
  );
}

export default Upload;
