# code from https://blog.joinmastodon.org/2018/06/how-to-implement-a-basic-activitypub-server/

require 'http'
require 'openssl'

# document      = File.read('activitypub/create-hello-world')
document      = File.read('activitypub/create-a-post.json')


# This is part is what's missing from the joinmastodon.org block post:
# It turns out there is a digest field the tutorial didn't go over. 
# This wasn't really clear to me from the blog post or any of the docs
# until I read the mastodon source code that each line in the 
# signed_string variable corresponds to one of the space-delimeted
# pseudo-headers specifieid in the "headers=" value of the header
# variable below. So since the pseudo headers list (request-target), 
# digest, host and date, there needs to be a line for each one in the
# signed_string variable before it get signed.
sha256 = OpenSSL::Digest::SHA256.new
digest = "SHA-256=" + Base64.strict_encode64(sha256.digest(document))


date          = Time.now.utc.httpdate
keypair       = OpenSSL::PKey::RSA.new(File.read('private.pem'))
signed_string = "(request-target): post /inbox\nhost: twit.social\ndate: #{date}\ndigest: #{digest}"
signature     = Base64.strict_encode64(keypair.sign(OpenSSL::Digest::SHA256.new, signed_string))
header        = 'keyId="https://jakekara.com/actors/jakekara.json#main-key",headers="(request-target) host date digest",signature="' + signature + '"'

print(document + "\n")
print(signed_string + "\n")

response = HTTP.headers({ 'Host': 'twit.social', 'Date': date, 'Signature': header, 'Digest': digest })
    .post('https://twit.social/inbox', body: document)

puts response