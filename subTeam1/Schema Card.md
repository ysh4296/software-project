# Schema card

| Use case UC-1 | Search  |
|--|--|
| Related Requirements |Req1, Req2, Req3, Req5  |
| Initiating Actor | 구매자  |
| Actor's Foal | 필터링, 정렬, 검색을 통해 원하는 가게 및 메뉴 찾기  |
| Participating Actors |  |
| Preconditions | 로그인이 되어있는 상태여야 한다.  |
| Post-conditions | 자신이 검색하고자 한 keyword에 포함되는 결과가 나열된다. 검색한 이후 결과에 대해서 필터링이 가능한 상태가 된다.|
| Preconditions | 로그인이 되어있는 상태여야 한다.  |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
 → 1. 구매자는 로그인 되어있는 상태이며, 피자 가게들의 리스트를 보여주는 url로 redirect한 상태.<br>
 → 2. 구매자는 자신이 검색하고자하는 검색어를 입력한다.<br>
 ← 3. 입력받은 검색어와 연관된 리스트를 구매자에게 보여주다.<br>
 → 4. 구매자는 검색 결과에 따른 리스트를 보고 메뉴를 선택한다.</td>
<table>
 <td colspan=""> Flow of Events for Extensions(Alternate Scenario): <br>
 2a. 구매자가 검색을 하지 않고 필터링 기능을 사용하여 자신이 원하는 결과를 찾을때<br>
 → 1. 구매자는 필터링 하고 싶은 키워드를 선택한다.<br>
 ← 2. 시스템은 그에 따른 리스트를 구매자에게 보여준다.<br>
 → 3. 구매자는 검색 결과에 따른 리스트를 보고 메뉴를 선택한다.<br><br>
 2b. 구매자는 정렬 기능을 사용하여 자신이 원하는 메뉴를 찾고자 할때<br>
 → 1. 구매자는 자신이 원하는 정렬 옵션(가격, 거리 등)을 선택한다.<br>
 ← 2. 시스템은 그에 따른 리스트를 구매자에게 보여준다.<br>
 → 3. 구매자는 검색 결과에 따른 리스트를 보고 메뉴를 선택한다.<br><br>
 3a. 입력받은 검색어와 연관된 리스트가 존재하지 않는 경우<br>
 ← 1. 연관된 검색어가 존재하지 않음을 알려주고 비어있는 리스트를 보여준다.<br>
 ← 2. 다시 검색이 가능하게 한다.
 </td>
</table>

| Use case UC-2 | Order  |
|--|--|
| Related Requirements |Req 10, Req11  |
| Initiating Actor | 구매자  |
| Actor's Foal | 자신이 검색해서 선택한 메뉴를 주문한다.  |
| Participating Actors | Shopping_Bag, Seller |
| Preconditions | 사용자로 로그인이 되어있어야 함. <br> 한 가지 이상의 메뉴가 장바구니에 들어가 있는 상태 <br> 피자 판매자가 등록한 영업시간일 때  |
| Post-conditions | 장바구니에 담긴 메뉴와 수량을 기반으로 총 주문 금액을 보여주고, 추가 전달사항 전달 뒤, 결제를 진행한다. |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1. 구매자는 로그인 되어 있는 상태이며, 한 가지 이상의 메뉴가 장바구니에 들어가 있는 상태에서 판매자에게 추가 전달사항이 있다면 작성한다.<br>
→ 2. 구매자는 자신이 결제할 방식을 선택한다.<br>
→ 3. 구매자는 결제 완료 버튼을 누른다.<br>
← 4. 시스템은 구매자가 작성한 추가 전달사항, 입력한 결제 방식, 주문 내용을 판매자에게 전달한다.</td>
<table>
 <td colspan=""> Flow of Events for Extensions(Alternate Scenario): <br>
3a. 인터넷 연결 불량 등의 이유로 정보가 판매자에게 제대로 전달되지 못한 경우.<br>
←1. 시스템은 구매자에게 정보를 다시 입력하기를 요구한다.<br>
→ 2. 구매자는 다시 한번 필요한 정보를 입력한다.<br>
← 3. 시스템은 다시 한번 입력된 정보를 판매자에게 재 전달한다.
 </td>
</table>

| Use case UC-3 | Mannage_Shopping_Bag  |
|--|--|
| Related Requirements |Req6, Req7, Req8  |
| Initiating Actor | 구매자  |
| Actor's Foal | Shopping bag(장바구니)를 관리한다.  |
| Participating Actors | Shopping_Bag |
| Preconditions | 로그인이 되어있어야 함. <br> 한 가지 이상의 메뉴를 선택한 상태여야함  |
| Post-conditions | 구매자가 원하는 메뉴와 수량이 들어있는 Shopping_Bag(장바구니) |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1. 구매자가 한개 이상의 메뉴를 선택하여 장바구니에 들어가 있는 상태<br>
→ 2. 구매자는 장바구니에 존재하는 메뉴 중에서 자신이 수정하고 싶은 메뉴를 선택<br>
← 3. 시스템은 구매자에게 메뉴를 어떻게 수정할 것인지 물어봄(수량, 삭제)<br>
→ 4. 구매자는 수량에 변화를 주거나, 삭제를 선택.<br>
← 5. 시스템은 결과를 반영하여 구매자에게 보여줌.</td>
<table>
 <td colspan=""> Flow of Events for Extensions(Alternate Scenario): <br>
2a. 장바구니에 존재하지 않는 메뉴를 추가하고자 하는 경우.<br>
→1. 구매자는 추가 버튼을 누른다.<br>
←2. 시스템은 추가가 가능한 메뉴를 보여준다.<br>
→3. 구매자는 추가 하고 싶은 메뉴를 선택하여 추가한다.<br>
←4. 시스템은 이를 반영하여 그 결과를 구매자에게 보여준다.
 </td>
</table>

| Use case UC-4 | Order_Info_Check  |
|--|--|
| Related Requirements |Req9, Req12  |
| Initiating Actor | 구매자  |
| Actor's Foal | 구매자는 자신의 주문내용 및 현재 배달 현황을 볼 수 있음  |
| Participating Actors | 구매자 |
| Preconditions | 구매자가 주문을 완료한 상태  |
| Post-conditions | 주문 현황 페이지로 이동 |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1. 구매자가 한개 이상의 메뉴를 선택하여 장바구니에 들어가 있는 상태<br>
→ 2. 구매자는 장바구니에 존재하는 메뉴 중에서 자신이 수정하고 싶은 메뉴를 선택<br>
← 3. 시스템은 구매자에게 메뉴를 어떻게 수정할 것인지 물어봄(수량, 삭제)<br>
→ 4. 구매자는 수량에 변화를 주거나, 삭제를 선택.<br>
← 5. 시스템은 결과를 반영하여 구매자에게 보여줌.</td>
<table>
 
 | Use case UC-5 | Delivery_Status_Update  |
|--|--|
| Related Requirements |Req13, Req14  |
| Initiating Actor | 판매자, 배달원 |
| Actor's Foal | 배달 현황을 업데이트(판매자의 주문수락 및 취소 포함)  |
| Participating Actors |  |
| Preconditions | 구매자가 주문을 완료한 상태  |
| Post-conditions | 배달이 완료되거나, 주문이 거절될 때까지 배달 현황이 업데이트 된다. |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1. UC-2(Order)을 포함한다.<br>
← 2. 시스템이 주문에 대한 정보와 수락여부 버튼을 화면에 띄운다.<br>
→ 3. 판매자가 ‘주문수락’ 버튼을 누른다.<br>
← 4. 시스템은 현재 배달현황을 ‘주문 수락’으로 업데이트 한다.<br>
→ 5. 피자가 완성되면 배달원이 피자를 픽업하고, ‘배달 중’ 버튼을 누른다.<br>
← 6. 시스템이 현재 배달현황을 ‘배달 중’으로 업데이트 한다.<br>
→ 7. 배달원이 구매자의 자택에 도착하면 배달완료 버튼을 누른다.<br>
→ 8. 시스템이 현재 배달현황을 ‘배달완료’ 로 업데이트 한다.</td>
<table>
 <td colspan=""> Flow of Events for Extensions(Alternate Scenario): <br>
→3a. 판매자가 ‘주문 거절’ 버튼을 클릭한다.<br>
←1. 시스템이 해당 주문을 취소시킨 후, 배달현황을 주문취소로 업데이트 한다.
 </td>
</table>

| Use case UC-6 | Cancel_Order  |
|--|--|
| Related Requirements |  |
| Initiating Actor | 구매자 |
| Actor's Foal | 주문을 취소하는 것  |
| Participating Actors |  |
| Preconditions | 판매자가 주문을 수학하기 점  |
| Post-conditions | 주문이 최소된다. |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1. 구매자가 ‘주문현황’ 페이지로 이동한다.<br>
← 2. 시스템이 구매자에게 구체적인 ‘주문현황’을 보여준다.<br>
→ 3. 구매자가 ‘주문 취소’ 버튼을 클릭한다.<br>
← 4. 시스템이 주문을 취소하고, 취소 결과를 화면에 띄운다.</td>
<table>
 
 | Use case UC-7 | Favorites  |
|--|--|
| Related Requirements | Req4 |
| Initiating Actor | 구매자 |
| Actor's Foal | 매장 및 메뉴에 대한 즐겨찾기 기능 이용  |
| Participating Actors |  |
| Preconditions | 구매자가 로그인이 되어있는 상태.  |
| Post-conditions | 선택한 매장 또는 메뉴가 구매자의 즐겨찾기 탭에 등록된다. 구매자는 추후에 즐겨찾기 탭에 등록된 매장 또는 메뉴에 바로 redirect할 수 있다. |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1.구매자는 로그인 되어있고 아직 즐겨찾기를 등록하지 않은 상태<br>
→ 2. 구매자가 피자집 또는 피자메뉴 위에 있는 즐겨찾기 버튼을 클릭<br>
← 3. 시스템이 해당 피자집 또는 메뉴를 즐겨찾기 탭에 등록</td>
<table>
 <td colspan=""> Flow of Events for Extensions(Alternate Scenario): <br>
1a. 구매자는 로그인 되어있고 즐겨찾기에 한가지 이상이 등록되어 있는 상태<br>
→1. 구매자는 즐겨찾기 탭을 누른다.<br>
←2. 시스템은 구매자를 ‘즐겨찾기’ 페이지로 redirect 시켜준다.<br>
→3. 구매자는 즐겨찾기에 등록된 메뉴가 매장을 누른다.<br>
←4. 시스템은 구매자를 해당하는 메뉴가 매장으로 redirect 시켜준다.
 </td>
</table>

 | Use case UC-8 | Menu_Add  |
|--|--|
| Related Requirements | Req6, Req8 |
| Initiating Actor | 구매자 |
| Actor's Foal | 메뉴를 장바구니에 추가하는 것(메뉴 선택)  |
| Participating Actors | 장바구니(Shopping bag) |
| Preconditions |  |
| Post-conditions | 구매자가 특정 메뉴를 선택할 때마다, 장바구니에 메뉴를 하나 씩 담는다. |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1. Search(O-UC1)을 포함한다.<br>
→ 2. 구매자는 검색된 피자집 리스트 중에서 원하는 곳을 클릭한다.<br>
← 3. 시스템이 선택된 피자집의 메뉴 리스트를 구매자에게 보여준다.<br>
→ 4. 구매자는 메뉴 리스트에서 메뉴 옆의 ‘장바구니 담기’ 버튼을 클릭한다.<br>
← 5. 시스템이 장바구니에 메뉴를 담는다.</td>
<table>
 
  | Use case UC-9 | Menu_Quantity_Change  |
|--|--|
| Related Requirements | Req8 |
| Initiating Actor | 구매자 |
| Actor's Foal | 장바구니에 있는 메뉴의 수량 변경  |
| Participating Actors | 장바구니(Shopping bag) |
| Preconditions | 장바구니에 적어도 1종류 이상의 메뉴가 담겨있다. |
| Post-conditions | 메뉴의 수량이 1씩 늘거나 줄어든다. |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1. 구매자가 장바구니에 담겨있는 메뉴 옆의 +버튼 또는 -버튼을 누른다.<br>
← 2. +를 누르면 수량이 1개 늘어나고, -를 누르면 수량이 1개 줄어든다.</td>
<table>
 <td colspan=""> Flow of Events for Extensions(Alternate Scenario): <br>
2a. 수량이 1개인 메뉴에서 -버튼을 누른다.<br>
← 1. 메뉴의 수량을 변경하지 않는다.
 </td>
</table>

 | Use case UC-10 | Menu_Delete  |
|--|--|
| Related Requirements | Req8 |
| Initiating Actor | 구매자 |
| Actor's Foal | 장바구니의 메뉴 삭제  |
| Participating Actors | 장바구니(Shopping bag) |
| Preconditions | 장바구니에 적어도 1종류 이상의 메뉴 존재 |
| Post-conditions | 장바구니에서 해당 메뉴가 삭제됨 |
<table>
<td colspan="">  Flow of Events for Main Success Scenario: <br>
→ 1. 구매자가 메뉴옆의 삭제 버튼을 누른다.<br>
← 2. 장바구니가 해당 메뉴를 삭제한다.</td>
<table>
