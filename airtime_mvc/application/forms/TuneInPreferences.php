<?php
require_once 'customvalidators/ConditionalNotEmpty.php';

class Application_Form_TuneInPreferences extends Zend_Form_SubForm
{
    public function init()
    {
        $this->setDecorators(array(
            array('ViewScript', array('viewScript' => 'form/preferences_tunein.phtml'))
        ));

        $enableTunein = new Zend_Form_Element_Checkbox("enable_tunein");
        $enableTunein->setDecorators(array(
            'ViewHelper',
            'Errors',
            'Label'
        ));
        $enableTunein->addDecorator('Label', array('class' => 'enable-tunein'));
        $enableTunein->setLabel(_("Push metadata to your station on TuneIn?"));
        $enableTunein->setValue(Application_Model_Preference::getTuneinEnabled());
        $enableTunein->setAttrib("class", "block-display");
        $this->addElement($enableTunein);

        $tuneinStationId = new Zend_Form_Element_Text("tunein_station_id");
        $tuneinStationId->setLabel(_("Station ID:"));
        $tuneinStationId->setValue(Application_Model_Preference::getTuneinStationId());
        $tuneinStationId->setAttrib("class", "input_text");
        $this->addElement($tuneinStationId);

        $tuneinPartnerKey = new Zend_Form_Element_Text("tunein_partner_key");
        $tuneinPartnerKey->setLabel(_("Partner Key:"));
        $tuneinPartnerKey->setValue(Application_Model_Preference::getTuneinPartnerKey());
        $tuneinPartnerKey->setAttrib("class", "input_text");
        $this->addElement($tuneinPartnerKey);

        $tuneinPartnerId = new Zend_Form_Element_Text("tunein_partner_id");
        $tuneinPartnerId->setLabel(_("Partner Id:"));
        $tuneinPartnerId->setValue(Application_Model_Preference::getTuneinPartnerId());
        $tuneinPartnerId->setAttrib("class", "input_text");
        $this->addElement($tuneinPartnerId);
    }

    public function isValid($data)
    {
        $valid = true;
        // Make request to TuneIn API to test the settings are valid.
        // TuneIn does not have an API to make test requests to check if
        // the credentials are correct. Therefore we will make a request
        // with the commercial flag set to true, which removes the metadata
        // from the station on TuneIn. After that, and if the test request
        // succeeds, we will make another request with the real metadata.
        if ($data["enable_tunein"]) {
            $qry_str = "?partnerId=".$data["tunein_partner_id"]."&partnerKey=".$data["tunein_partner_key"]."&id=".$data["tunein_station_id"];
            $commercialFlagQryStr = "&commercial=true";

            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, TUNEIN_API_URL . $qry_str . $commercialFlagQryStr);
            curl_setopt($ch, CURLOPT_FAILONERROR, 1);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_TIMEOUT, 30);

            $xmlData = curl_exec($ch);
            if (curl_error($ch)) {
                Logging::error("Failed to reach TuneIn: ". curl_errno($ch)." - ". curl_error($ch) . " - " . curl_getinfo($ch, CURLINFO_EFFECTIVE_URL));
                if (curl_error($ch) == "The requested URL returned error: 403 Forbidden") {
                    $this->getElement("enable_tunein")->setErrors(array(_("Invalid TuneIn Settings. Please ensure your TuneIn settings are correct and try again.")));

                    $valid = false;
                }
            }
            curl_close($ch);

            if ($valid) {
                $xmlObj = new SimpleXMLElement($xmlData);
                if (!$xmlObj || $xmlObj->head->status != "200") {
                    $valid = false;
                } else if ($xmlObj->head->status == "200") {
                    $valid = true;

                    // Make another request to TuneIn to update the metadata right away
                    // and to turn off the commercial flag.

                    $metadata = Application_Model_Schedule::getCurrentPlayingTrack();

                    if (!is_null($metadata)) {

                        Logging::info($metadata);
                        // Replace empty strings with "n/a" since the TuneIn API will complain
                        // and return an error that title and/or artist is not set.
                        $metadata["artist"] = empty($metadata["artist"]) ? "n/a" : $metadata["artist"];
                        $metadata["title"] = empty($metadata["title"]) ? "n/a" : $metadata["title"];
                        Logging::info($metadata);

                        $metadataQryStr = "&artist=" . $metadata["artist"] . "&title=" . $metadata["title"];

                        $ch = curl_init();
                        curl_setopt($ch, CURLOPT_URL, TUNEIN_API_URL . $qry_str . "&commercial=false" . $metadataQryStr);
                        curl_setopt($ch, CURLOPT_FAILONERROR, 1);
                        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
                        curl_setopt($ch, CURLOPT_TIMEOUT, 30);

                        $xmlData = curl_exec($ch);
                        Logging::info($xmlData);
                        if (curl_error($ch)) {
                            Logging::error("Failed to reach TuneIn: " . curl_errno($ch) . " - " . curl_error($ch) . " - " . curl_getinfo($ch, CURLINFO_EFFECTIVE_URL));
                        }

                        curl_close($ch);
                        $xmlObj = new SimpleXMLElement($xmlData);
                        if (!$xmlObj || $xmlObj->head->status != "200") {
                            Logging::error("Failed updating metadata on TuneIn");
                        }
                    }

                }
            }
        } else {
            $valid = true;
        }

        if (!$valid) {
            // Set values to what the user entered since the form is invalid so they
            // don't have to enter in the values again and can see what they entered.
            $this->getElement("enable_tunein")->setValue($data["enable_tunein"]);
            $this->getElement("tunein_partner_key")->setValue($data["tunein_partner_key"]);
            $this->getElement("tunein_partner_id")->setValue($data["tunein_partner_id"]);
            $this->getElement("tunein_station_id")->setValue($data["tunein_station_id"]);
        }

        return $valid;
    }
}
