
from lxml import etree


pro=[1,2,3,4,5,6]
root = etree.Element('products')
for i in pro:
    i=i+7
    productid='product'+str(i)
    product = etree.Element(productid)

    productprice='price'+str(i)
    """productprice"""
    productp=etree.Element('productprice')
    productp.text=productprice
    """productprice"""

    productname='productname'+str(i)
    """productname"""
    productn=etree.Element('productname')
    productn.text=productname
    """productname"""

    product.append(productn)
    product.append(productp)
    root.append(product)

with open('file.xml', 'a') as f:
    f.write(etree.tostring(root).decode("ascii"))
    f.close()
