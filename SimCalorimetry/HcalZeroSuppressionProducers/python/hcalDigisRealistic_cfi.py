# to use the ZS thresholds from config file, 
# set useConfigZSvalues = cms.int32(1)
# to generate Unsuppressed digis, 
# also need to set useConfigZSvalues = cms.int32(1) and -inf. (-999) levels
# to use the channel-by-channel ZS values from DB, 
# set useConfigZSvalues = cms.int32(0) - default

import FWCore.ParameterSet.Config as cms

simHcalDigis = cms.EDProducer("HcalRealisticZS",
    digiLabel = cms.string("simHcalUnsuppressedDigis"),
    markAndPass = cms.bool(False),
    HBlevel = cms.int32(8),
    HElevel = cms.int32(9),
    HOlevel = cms.int32(24),
    HFlevel = cms.int32(-9999),
    HBregion = cms.vint32(3,6),      
    HEregion = cms.vint32(3,6),
    HOregion = cms.vint32(1,8),
    HFregion = cms.vint32(2,3),      
    useConfigZSvalues = cms.int32(0)
)

from Configuration.Eras.Modifier_phase2_hcal_cff import phase2_hcal
phase2_hcal.toModify( simHcalDigis,
                             useConfigZSvalues = cms.int32(1),
                             HElevel = cms.int32(3)
)

from Configuration.Eras.Modifier_run2_HF_2017_cff import run2_HF_2017
run2_HF_2017.toModify( simHcalDigis,
                             HFregion = cms.vint32(1,2)
)

from Configuration.Eras.Modifier_run2_HB_2018_cff import run2_HB_2018
run2_HB_2018.toModify( simHcalDigis,
                             HBregion = cms.vint32(2,5)
)

from Configuration.Eras.Modifier_run2_HE_2018_cff import run2_HE_2018
run2_HE_2018.toModify( simHcalDigis,
                             HEregion = cms.vint32(2,5)
)

