import pandas as pd
from bs4 import BeautifulSoup
table = """
<table border="0" cellpadding="0" cellspacing="0" class="table table-borderd sm-table" width="100%">
<tbody>
<tr>
<th>길이1</th>
<td><input class="form-control" id="clo_warp_stretch_height[0]" name="clo_warp_stretch_height[0]" placeholder="" readonly="" type="text" value="5"/></td>
<th>힘1</th>
<td><input class="form-control" id="clo_warp_stretch_strength[0]" name="clo_warp_stretch_strength[0]" placeholder="" readonly="" type="text" value="0.028"/></td>
</tr>
<tr>
<th>길이2</th>
<td><input class="form-control" id="clo_warp_stretch_height[1]" name="clo_warp_stretch_height[1]" placeholder="" readonly="" type="text" value="10"/></td>
<th>힘2</th>
<td><input class="form-control" id="clo_warp_stretch_strength[1]" name="clo_warp_stretch_strength[1]" placeholder="" readonly="" type="text" value="0.055"/></td>
</tr>
<tr>
<th>길이3</th>
<td><input class="form-control" id="clo_warp_stretch_height[2]" name="clo_warp_stretch_height[2]" placeholder="" readonly="" type="text" value="15"/></td>
<th>힘3</th>
<td><input class="form-control" id="clo_warp_stretch_strength[2]" name="clo_warp_stretch_strength[2]" placeholder="" readonly="" type="text" value="0.086"/></td>
</tr>
<tr>
<th>길이4</th>
<td><input class="form-control" id="clo_warp_stretch_height[3]" name="clo_warp_stretch_height[3]" placeholder="" readonly="" type="text" value="20"/></td>
<th>힘4</th>
<td><input class="form-control" id="clo_warp_stretch_strength[3]" name="clo_warp_stretch_strength[3]" placeholder="" readonly="" type="text" value="0.125"/></td>
</tr>
<tr>
<th>길이5</th>
<td><input class="form-control" id="clo_warp_stretch_height[4]" name="clo_warp_stretch_height[4]" placeholder="" readonly="" type="text" value="30"/></td>
<th>힘5</th>
<td><input class="form-control" id="clo_warp_stretch_strength[4]" name="clo_warp_stretch_strength[4]" placeholder="" readonly="" type="text" value="0.2"/></td>
</tr>
<tr>
<th>길이6</th>
<td><input class="form-control" id="clo_warp_stretch_height[5]" name="clo_warp_stretch_height[5]" placeholder="" readonly="" type="text" value="0"/></td>
<th>힘6</th>
<td><input class="form-control" id="clo_warp_stretch_strength[5]" name="clo_warp_stretch_strength[5]" placeholder="" readonly="" type="text" value="0"/></td>
</tr>
<tr>
<th>길이7</th>
<td><input class="form-control" id="clo_warp_stretch_height[6]" name="clo_warp_stretch_height[6]" placeholder="" readonly="" type="text" value="0"/></td>
<th>힘7</th>
<td><input class="form-control" id="clo_warp_stretch_strength[6]" name="clo_warp_stretch_strength[6]" placeholder="" readonly="" type="text" value="0"/></td>
</tr>
<tr>
<th>길이8</th>
<td><input class="form-control" id="clo_warp_stretch_height[7]" name="clo_warp_stretch_height[7]" placeholder="" readonly="" type="text" value="0"/></td>
<th>힘8</th>
<td><input class="form-control" id="clo_warp_stretch_strength[7]" name="clo_warp_stretch_strength[7]" placeholder="" readonly="" type="text" value="0"/></td>
</tr>
<tr>
<th>길이9</th>
<td><input class="form-control" id="clo_warp_stretch_height[8]" name="clo_warp_stretch_height[8]" placeholder="" readonly="" type="text" value="0"/></td>
<th>힘9</th>
<td><input class="form-control" id="clo_warp_stretch_strength[8]" name="clo_warp_stretch_strength[8]" placeholder="" readonly="" type="text" value="0"/></td>
</tr>
<tr>
<th>길이10</th>
<td><input class="form-control" id="clo_warp_stretch_height[9]" name="clo_warp_stretch_height[9]" placeholder="" readonly="" type="text" value="0"/></td>
<th>힘10</th>
<td><input class="form-control" id="clo_warp_stretch_strength[9]" name="clo_warp_stretch_strength[9]" placeholder="" readonly="" type="text" value="0"/></td>
</tr>
</tbody>
</table>
"""

table_object = BeautifulSoup(table,  "html.parser")
trs = table_object.find_all("tr")


result = []

for tr in trs:
    tds = tr.find_all("td")
    tr_value = []
    for td in tds:
        td_input = td.find("input")
        tr_value.append(td_input.get('value'))

    result.append(tr_value)

print(result)
