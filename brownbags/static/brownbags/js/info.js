function info(self) {
    var index = parseInt(self.data.index);
    var item = getShopItem(index);

    // 店名設定
    var name = item["name"];
    self.querySelector('ons-toolbar .center').innerHTML = name;
    self.querySelector('#shop_name').textContent = name;

    // 店舗画像
    $("#image_name").html(get_image_html("image_name", item["images"]["name"]));

    // ジャンル
    self.querySelector('#shop_genre').textContent = get_genre_sel_name(item["genre_sel"]);

    // 店舗概要
    if (!isEmpty(item["description"]))
        self.querySelector('#shop_description').textContent = item["description"];

    // メニュー情報
    $("#image_takeway").html(get_image_html("image_takeway", item["images"]["takeaway"]));

    // テイクアウト（持ち帰り）
    self.querySelector('#shop_takeaway_sel').textContent = get_takeaway_sel_name(item["takeaway_sel"]);

    // テイクアウト（持ち帰り）メニュー
    if (!isEmpty(item["takeaway_menu"]))
        self.querySelector('#shop_takeaway_menu').innerHTML = conv_br(item["takeaway_menu"]);

    // テイクアウトに関してのお知らせ
    if (!isEmpty(item["takeaway_note"]))
        self.querySelector('#shop_takeaway_note').innerHTML = conv_br(item["takeaway_note"]);

    // デリバリーサービス（出前・配達）
    self.querySelector('#shop_delivery').textContent = get_delivery(item);

    // デリバリーサービス（出前・配達）関してのお知らせ
    if (!isEmpty(item["delivery_note"]))
        self.querySelector('#shop_delivery_note').innerHTML = conv_br(item["delivery_note"]);

    // 電話番号
    var phone = item["phone"];
    if (!isEmpty(phone))
        $("#shop_phone").html('<address><a href="tel:' + phone + '">' + phone + '</a></address>');

    // 定休日・営業時間
    if (!isEmpty(item["open_day"]))
        self.querySelector('#shop_open_day').innerHTML = conv_br(item["open_day"]);

    // 住所
    if (!isEmpty(item["addr_sel"]) && !isEmpty(item["addr"]))
        self.querySelector('#shop_addr').textContent = item["addr_sel"] + item["addr"];
    else if (!isEmpty(item["addr_sel"]) && isEmpty(item["addr"]))
        self.querySelector('#shop_addr').textContent = item["addr_sel"];
    else if (isEmpty(item["addr_sel"]) && !isEmpty(item["addr"]))
        self.querySelector('#shop_addr').textContent = item["addr"];

    // Webサイト>
    var website = item["website"];
    if (!isEmpty(website)) {
        $("#shop_website").html('<a href="' + website + '" target="_blank" rel="noopener noreferrer">' + website + '</a>');
    }

    // SNS
    var twitter = item["twitter"];
    if (!isEmpty(twitter))
        $("#shop_twitter").html('<a href="https://twitter.com/' + twitter + '" target="_blank" rel="noopener noreferrer">' + twitter + '</a>');

    var facebook = item["facebook"];
    if (!isEmpty(facebook))
        $("#shop_facebook").html('<a href="https://www.facebook.com/' + facebook + '" target="_blank" rel="noopener noreferrer">' + facebook + '</a>');

    var instagram = item["instagram"];
    if (!isEmpty(instagram))
        $("#shop_instagram").html('<a href="https://www.instagram.com/' + instagram + '" target="_blank" rel="noopener noreferrer">' + instagram + '</a>');

    if (!isEmpty(item["line"]))
        self.querySelector('#shop_line').textContent = item["line"];
    if (!isEmpty(item["sns_other"]))
        self.querySelector('#shop_sns_other').textContent = item["sns_other"];

    // 支払い方法
    self.querySelector('#shop_payment').textContent = get_payment(item);

    // 支払い方法に関してのお知らせ
    if (!isEmpty(item["payment_note"]))
        self.querySelector('#shop_payment_note').innerHTML = conv_br(item["payment_note"]);

    // アクセス・交通手段
    if (!isEmpty(item["transportation"]))
        self.querySelector('#shop_transportation').innerHTML = conv_br(item["transportation"]);

    // ベジタリアン
    if (!isEmpty(item["diet_note"]))
        self.querySelector('#shop_diet_note').innerHTML = conv_br(item["diet_note"]);

    // アレルギー
    if (!isEmpty(item["allergy_note"]))
        self.querySelector('#shop_allergy_note').innerHTML = conv_br(item["allergy_note"]);

    // covid19
    if (!isEmpty(item["covid19_note"]))
        self.querySelector('#shop_covid19_note').innerHTML = conv_br(item["covid19_note"]);

    // メモ
    if (!isEmpty(item["note"]))
        self.querySelector('#shop_note').innerHTML = conv_br(item["note"]);

    // マップ
    var lat = item["latitude"];
    var lon = item["longitude"];
    map_info(lat, lon, name);
}
function conv_br(str) {
    var text = str.replace(/\r?\n/g, '<br>');
    return text;
}

/* slick
 Version: 1.6.0
  Author: Ken Wheeler
 Website: http://kenwheeler.github.io
    Docs: http://kenwheeler.github.io/slick
    Repo: http://github.com/kenwheeler/slick
  Issues: http://github.com/kenwheeler/slick/issues
slick.jsの使い方まとめ
    http://cly7796.net/wp/javascript/plugin-slick/
Doc
    https://kenwheeler.github.io/slick/
*/
function get_image_html(selector, images_name) {
    var html_deffault = '<div class="camera"><div class="focus"></div></div>';

    for (var ii=0; ii<images_name.length; ii++) {
        var imageurl = get_image_url(images_name[ii], null);
        if (!imageurl) {
            imageurl = html_deffault;
        }
        //var html = '<div class="" style="border:1px"><img src="' + imageurl + '" style="width:70%;height:200px"></div>';
        var html = '<div class="" style="border:1px"><img src="' + imageurl + '" style="height:300px"></div>';
        $("#" + selector).append(html);
    }

    $("#" + selector).slick({
        slidesToShow: 1,
        slidesToScroll: 2,
        centerMode: true,
        centerPadding: '0px',
        dots: true,
        infinite: true,
        speed: 500,
        //fade: true,
        cssEase: 'linear'
    });

}