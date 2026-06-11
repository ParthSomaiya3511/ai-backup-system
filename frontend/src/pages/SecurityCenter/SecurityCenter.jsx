import MainLayout
from "../../components/layout/MainLayout";

export default function SecurityCenter() {

  return (

    <MainLayout>

      <h1>

        Security Center

      </h1>

      <ThreatScoreCard
        score={92}
      />

    </MainLayout>

  );

}