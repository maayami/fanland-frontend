import React, { useEffect, useState } from "react";
import { NavLink, useRouteMatch } from "react-router-dom";
import Club from "../club";
import { useAuth } from "../../auth/useAuth";
import djangoRESTAPI from "../../api/djangoRESTAPI";

export default function DefaultPreview({ title, endpoint, tags }) {
  let { url } = useRouteMatch();
  const auth = useAuth();
  const [data, setData] = useState([]);
  const [isLoading, setLoading] = useState(true);

  const fetchClubs = async () => {
    await djangoRESTAPI
      .get(`userdetails/${auth.user.id}/${endpoint}`)
      .then((res) => {
        res.data.map((clubId) => {
          djangoRESTAPI
            .get(`fanclubs_basic/${clubId}`)
            .then((res) => setData((data) => [...data, res.data]));
        });
      })
      .catch((err) => {
        console.log(err);
      });
    setLoading(false);
  };

  useEffect(() => {
    fetchClubs();
  }, [endpoint, tags]);

  return isLoading ? (
    <div>Loading...</div>
  ) : (
    <div className="px-3 overflow-auto container-home">
      <div>
        <p className="pt-5 fs-large fw-bolder ">{title}</p>
      </div>
      <div>
        {tags ? (
          <div className="d-flex my-4">
            {tags.map((tag, index) => {
              let link = index === 0 ? url : url + "/" + tag.tagId;
              return (
                <NavLink
                  exact
                  key={index}
                  to={link}
                  className="link mx-2 text-white py-1"
                  activeClassName="tag-navlink-active"
                >
                  {tag.tagTitle}
                </NavLink>
              );
            })}
          </div>
        ) : (
          <div className="py-3"></div>
        )}
        {/* <p className="fw-bold pb-1"></p> */}
        <div className="custom-border-top pt-3">
          <div className="clubs-container">
            {data.map((dataItem) => {
              return (
                <Club
                  key={dataItem.id}
                  clubName={dataItem.name}
                  clubDes={dataItem.des}
                  clubId={dataItem.id}
                  imageurl={dataItem.image}
                />
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
