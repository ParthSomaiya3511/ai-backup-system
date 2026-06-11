export default function RecentActivity() {

  const activities = [

    "Backup Created",

    "File Restored",

    "AI Scan Completed",

    "Threat Scan Completed"

  ];

  return (

    <div className="bg-slate-800 p-5 rounded-xl">

      <h2>

        Recent Activity

      </h2>

      {

        activities.map((item, index) => (

          <p key={index}>

            {item}

          </p>

        ))

      }

    </div>

  );

}