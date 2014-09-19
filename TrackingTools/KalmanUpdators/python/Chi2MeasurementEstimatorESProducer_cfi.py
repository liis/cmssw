import FWCore.ParameterSet.Config as cms

Chi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(30.0)
)

Chi2MeasurementEstimatorAsym = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
                                              ComponentName = cms.string('Chi2A'),
                                              nSigma = cms.double(1.0),
                                              MaxChi2 = cms.double(1.0)
                                              )


