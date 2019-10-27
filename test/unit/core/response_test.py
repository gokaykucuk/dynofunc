
from dynamof.core.response import destructure_type_tree, response


def test_destructure_handles_none():

    assert destructure_type_tree(None) == None

def test_response_uses_destructure():
    mock_boto_response = {
        'Item': {
          "features": {
            "L": [
              { "S": "glow" },
              { "S": "dust" }
            ]
          }
        }
    }

    item = response(mock_boto_response).item()

    assert len(item.get('features')) == 2
