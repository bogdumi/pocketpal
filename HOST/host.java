import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.rest.api.v2010.account.Call;
import com.twilio.type.PhoneNumber;

import java.net.URI;

public class Host {
    // Find your Account Sid and Token at twilio.com/console
    // DANGER! This is insecure. See http://twil.io/secure
    public static final String ACCOUNT_SID = "ACf627d2336806adfa6b0475e9739babaf";
    public static final String AUTH_TOKEN = "1abf3c0296584cc5f7114359313f048f";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        Message message = Message.creator(
                new com.twilio.type.PhoneNumber("+447723569692"),
                new com.twilio.type.PhoneNumber("+447342178041"),
                "This is the ship that made the Kessel Run in fourteen parsecs?")
            .create();
        Call call = Call.creator(
                new com.twilio.type.PhoneNumber("+447723569692"),
                new com.twilio.type.PhoneNumber("+447342178041"),
                URI.create("http://demo.twilio.com/docs/voice.xml"))
            .create();


        System.out.println(message.getSid());
    }
}