# code from https://blog.joinmastodon.org/2018/06/how-to-implement-a-basic-activitypub-server/

require 'http'
require 'openssl'

document      = File.read('activitypub/create-hello-world')
# It turns out there is a digest field the tutorial didn't go over. This seems to be
# the right way to compute it because other attempts were failing. 
sha256 = OpenSSL::Digest::SHA256.new
digest = Base64.strict_encode64(sha256.digest(document))


date          = Time.now.utc.httpdate
keypair       = OpenSSL::PKey::RSA.new(File.read('private.pem'))
signed_string = "(request-target): post /inbox\ndigest: SHA-256=#{digest}\nhost: twit.social\ndate: #{date}"
signature     = Base64.strict_encode64(keypair.sign(OpenSSL::Digest::SHA256.new, signed_string))
header        = 'keyId="https://jakekara.com/actor#main-key",headers="(request-target) digest host date",signature="' + signature + '"'

print(document + "\n")
print(signed_string + "\n")

response = HTTP.headers({ 'Host': 'twit.social', 'Date': date, 'Signature': header, 'Digest': "SHA-256="+digest })
    .post('https://twit.social/inbox', body: document)

puts response