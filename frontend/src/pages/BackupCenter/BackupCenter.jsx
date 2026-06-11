import MainLayout from "../../components/layout/MainLayout";

export default function BackupCenter() {

  const backups = [

    {
      file: "project.zip",
      version: "v5",
      date: "2026-06-11"
    },

    {
      file: "report.docx",
      version: "v3",
      date: "2026-06-10"
    }

  ];

  return (

    <MainLayout>

      <h1 className="text-2xl mb-6">

        Backup Center

      </h1>

      <table>

        <thead>

          <tr>

            <th>File</th>

            <th>Version</th>

            <th>Date</th>

          </tr>

        </thead>

        <tbody>

          {backups.map((item,index)=>(

            <tr key={index}>

              <td>{item.file}</td>

              <td>{item.version}</td>

              <td>{item.date}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </MainLayout>

  );

}