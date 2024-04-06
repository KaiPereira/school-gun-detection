import { useEffect, useState } from "react";


export default function Home() {
  const [calls, setcalls] = useState()

  useEffect(() => {
    // Fetch the image calls from the server-side endpoint
    fetch('/api/get-calls')
      .then(response => response.json())
      .then(data => {
          // Update the src attribute of the img element with the retrieved image calls
          setcalls(data)
      })
      .catch(error => {
          console.error('Error fetching detected image:', error);
      });
  }, [])

  console.log(calls)

  return (
    <>{ calls &&
      <div className="flex gap-5 p-4">
      {
        calls.map((call, index) => {

          return (
            <div key={index} className="p-4 rounded-md shadow-xl border-2 flex flex-col gap-4">
              { (call.where.length > 100) ?
                <img src={`data:image/jpeg;base64,${call.where}`} alt="Detected Image" className="rounded w-72 border-2"/>
                :
                <p>{call.where}</p>
              }
              <p className="text-lg font-bold">{call.why}</p>
              <p>Called police: {call.when}</p>
            </div>
          )
        })
      }
      </div>
  }</>
  );
}
