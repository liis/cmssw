import FWCore.ParameterSet.Config as cms

process = cms.Process("reGsfTracking")

# message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger = cms.Service("MessageLogger",
                                         default = cms.untracked.PSet( limit = cms.untracked.int32(-1) )
                                    )

# source
readFiles = cms.untracked.vstring()

secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",
                     fileNames=cms.untracked.vstring(
    'file:108E0ACE-C1B4-E311-BAE4-0025904E9010.root' 
    ),
#                     secondaryFileNames=cms.untracked.vstring( #Provide corresponding DIGI files for tracking particles
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/02A8EF51-62D1-E311-9270-02163E00EB1C.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/22360CB9-62D1-E311-AAC8-02163E00E8F4.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/2C4CD1E2-62D1-E311-840A-02163E00EA17.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/2CC8BC3A-62D1-E311-80C4-02163E00EAC3.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/3E92DFF4-62D1-E311-B169-02163E00E83C.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/4AF6D3E5-62D1-E311-BB13-02163E00F335.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/4E9486E1-62D1-E311-B091-02163E00EB07.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/563694CA-62D1-E311-B8B7-02163E00E9F6.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/6A17CF7C-62D1-E311-A943-02163E00E6D6.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/76B6063A-72D1-E311-95E6-02163E00CDE3.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/9E65F9A2-62D1-E311-8D37-02163E00E8D2.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/9EA489AB-62D1-E311-9A1A-02163E00E776.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/AE3BAC91-62D1-E311-B275-02163E00E869.root',
#    'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/C637DD05-63D1-E311-A4FB-02163E00EAC7.root',
 #   'file:/hdfs/cms/store/user/liis/El_GSF_studies/Zee_7_1_0_pre7_PU50_DIGI/DE0B8342-62D1-E311-AECF-02163E00EA85.root',       
#                     )
                     )

process.source = source
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

### conditions
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#process.GlobalTag.globaltag = 'PRE_MC_71_V2'
### standard includes

## Geometry and Detector Conditions (needed for a few patTuple production steps)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup')
process.GlobalTag.globaltag = 'PRE_STA71_V2::All'


process.load('Configuration/StandardSequences/Services_cff')
process.load("Configuration.Geometry.GeometryIdeal_cff")

process.load('Configuration.StandardSequences.GeometryPilot2_cff')
process.load("Configuration.StandardSequences.RawToDigi_cff")

process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("Configuration.StandardSequences.Reconstruction_cff")



from SimGeneral.MixingModule.trackingTruthProducer_cfi import *

#process.TrajectoryBuilderForElectrons.estimator = cms.string('Chi4A')

maxCandDefault = 5
maxChi2Default = 2000
nSigmaDefault = 3.0

maxCand = 6
maxChi2 = 100
nSigma = 4

########################################################################
# to change parameters  as in slides from A.Tropiano


process.TrajectoryBuilderForElectrons.maxCand = cms.int32( maxCand )
process.ElectronChi2.MaxChi2 = cms.double( maxChi2 )
process.ElectronChi2.nSigma = cms.double( nSigma )

########################################################################

#process.GlobalPaositionSource = cms.ESSource("PoolDBESSource",
#                                            process.CondDBSetup,
#                                            # Reading from oracle (instead of Frontier) needs the following shell variable setting (in zsh):
#                                            # export CORAL_AUTH_PATH=/afs/cern.ch/cms/DB/conddb
#                                            # string connect = "oracle://cms_orcoff_int2r/CMS_COND_ALIGNMENT"
#                                            # untracked uint32 authenticationMethod = 1
#                                            toGet = cms.VPSet(cms.PSet(
#    record = cms.string('GlobalPositionRcd'),
#    tag = cms.string('IdealGeometry')
#    )),
#                                            connect = cms.string('sqlite_file:output.db')
#                                            )





process.printEventContent = cms.EDAnalyzer("EventContentAnalyzer")
# sequence for re-running gsfTracking over RECO
process.myGsfReco = cms.Sequence(
########    process.localreco
    process.siPixelRecHits*
    process.siStripMatchedRecHits* #make local hits
    process.MeasurementTrackerEvent* #ADD
    process.iterTracking*
    process.printEventContent*
    process.electronSeedsSeq #ADD
########    process.trackCollectionMerging  #REMOVE
########    process.newCombinedSeeds* # contained in electronSeedSeq 
#    process.electronSeeds*    #produced merged collection of TkDriven and Ecaldriven seeds
#    process.electronCkfTrackCandidates*process.electronGsfTracks #run electron tracking
########   process.mix
)

outdir = "out_tests/"
outfilename = outdir + "reGsfTracking_maxCand_" + str(maxCand) + "_MaxChi2_" + str(maxChi2) + "_nSigma_" + str(nSigma) + ".root"
print "Writing output to file: " + outfilename

process.TFileService = cms.Service("TFileService", # if save
                                   fileName = cms.string(outfilename)
                                   )


#---------------- high purity selection of reco::Tracks---------------
process.load("PhysicsTools.RecoAlgos.recoTrackSelector_cfi")
process.cutsRecoTracksHp = process.recoTrackSelector.clone()
process.cutsRecoTracksHp.quality = cms.vstring("highPurity")
process.cutsRecoTracksHp.minAbsEta = cms.double(0.0)
process.cutsRecoTracksHp.maxAbsEta = cms.double(2.5)


process.ValidationSelectors = cms.Sequence(
        process.cutsRecoTracksHp
            )

#--------------------------- tree maker --------------------------
#process.load("MakeTree.MakeTrackValTree.maketrackvaltree_cfi") # for writing output to a flat tree

process.printEventContent = cms.EDAnalyzer("EventContentAnalyzer")

# paths
process.p = cms.Path(
    process.myGsfReco 
#    process.ValidationSelectors * 
#    process.printEventContent 
#    process.trackValTreeMaker
    )


process.schedule = cms.Schedule(
    process.p
    )
